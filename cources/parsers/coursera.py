import time
import requests
from bs4 import BeautifulSoup

from cources.models import Tags, Courses, Provider, Author, CourseAuthor
from cources.tasks import CourseScrapperBase


class CourseraCourseScraper(CourseScrapperBase):
    def __init__(self, tag_id):
        self.tag_id = tag_id
        super().__init__("https://www.coursera.org/courses", "Coursera")

    @property
    def tag_title(self):
        return Tags.objects.get(id=self.tag_id)

    @property
    def search_url(self):
        return f'{self.url_base}?query={self.tag_title}'

    def scrap(self):
        all_courses = []
        for tab_num in range(1, 4):
            response = requests.get(f'{self.search_url}&page={tab_num}')
            soup = BeautifulSoup(response.text, "html.parser")
            with open("courses.html", "w", encoding="utf-8") as file:
                file.write(soup.prettify())
            courses_data = self._parse_courses(soup)
            all_courses.append(courses_data)

        return all_courses

    def _parse_courses(self, soup):
        course_cards = soup.select("div.cds-ProductCard-gridCard")

        courses = []
        for card in course_cards:
            # Get course link
            link_tag = card.find("a", href=True)
            if not link_tag:
                continue
            course_link = f"https://www.coursera.org{link_tag['href']}"

            # Get course image
            image_tag = card.select_one("div.cds-CommonCard-previewImage img")
            image_url = image_tag["src"] if image_tag and "src" in image_tag.attrs else "Image not found"

            course_data = self._get_course_data(course_link)
            if course_data:
                course_data["image_url"] = image_url
                course_data["course_url"] = course_link
                self.save_course(course_data)

                courses.append(course_data)
            time.sleep(2)

        return courses

    def save_course(self, course_data: dict):
        is_course_exists = Courses.objects.filter(
            canonical_url=course_data['course_url']).exists()
        if is_course_exists:
            return False

        course = Courses(
            title=course_data['title'],
            title_en=course_data['title'],
            provider=Provider.objects.get(code='COURSERA'),
            summary=course_data.get('summary', ''),
            cover=course_data.get('image_url', ''),
            total_units=course_data.get('total_units', 0),
            acquired_skills=course_data.get('acquired_skills', ''),
            acquired_assets=course_data.get('acquired_assets', ''),
            is_active=True
        )
        course.save()

        author, _ = Author.objects.get_or_create(
            title=course_data['company']
        )
        CourseAuthor.objects.create(
            course=course, author=author
        )

        return course

    def _get_course_data(self, course_url):
        try:
            response = requests.get(course_url)
            if response.status_code != 200:
                return None

            soup = BeautifulSoup(response.text, "html.parser")

            # Save page content for analysis
            with open("course_page.html", "w", encoding="utf-8") as file:
                file.write(soup.prettify())

            title = soup.select_one("h1").text if soup.select_one("h1") else "N/A"
            acquired_skills = [
                p.text for p in soup.select("div[data-track-component='what_you_will_learn_section'] p")
            ]
            acquired_assets = [
                li.text for li in soup.select("div[data-track-component='career_outcomes'] li")
            ]
            rating_div = soup.find("div", {"aria-label": lambda x: x and "stars" in x})
            rating = rating_div.get_text(strip=True) if rating_div else "Рейтинг не найден"

            company = 'not found'
            offered_by_section = soup.find('h3', string="Offered by")
            if offered_by_section:
                parent_div = offered_by_section.find_next('div', class_='css-1f454bp')
                if parent_div:
                    company_name = parent_div.find('span', class_='css-6ecy9b') or parent_div.find('span', class_='cds-119')
                    company = company_name.get_text(strip=True) if company_name else "not found"
            course_summary = soup.find('p', class_='css-4s48ix').get_text(strip=True)
            if course_summary and course_summary.startswith('Instructors'):
                course_summary = None

            total_units = soup.find('div', class_='css-fk6qfz').get_text(strip=True)

            # learning_format_div = soup.find('div', class_='cds-170')
            # learning_format = ''
            # if learning_format_div:
            #     learning_format = ", ".join([li.text for li in learning_format_div.select("div[class='css-dwgey1']")[-1].select("div")[1:]])

            course_info = {
                "title": title,
                "acquired_skills": acquired_skills,
                "rating": rating,
                "company": company,
                "summary": course_summary,
                "total_units": total_units,
                "acquired_assets": acquired_assets,
                # "learning_format": learning_format,
            }
            return course_info

        except Exception as e:
            return None

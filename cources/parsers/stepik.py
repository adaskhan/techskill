import requests

from cources.models import Courses, Provider, Sections, Lessons, Units, Assignments, Steps
from cources.tasks import CourseScrapperBase


class StepikCourseScrapper(CourseScrapperBase):
    def __init__(self, tag_id):
        self.tag_id = tag_id
        super().__init__("https://stepik.org/api/", "Stepik")

    def scrap(self):
        token = self.get_access_token()
        courses_data = self.get_courses_by_tag(token)
        new_courses = []
        for course_data in courses_data:
            course = self.save_course(course_data)
            if not course:
                continue

            self.scrap_course_details(course, token, course_data['sections'])
            new_courses.append(course)

        return new_courses

    @staticmethod
    def get_access_token():
        client_id = 'qGlHPrLQCd0235gNV1GK6cbTu2pXxhE4eEJIZ3xK'
        client_secret = 'AfdLSihXnMgmGYTfm9T1ym7qb4mvmQMfHp6mpCeiCJaxfbLEtfZPxZIEbzQiN9woUoFzZeKzW1Z96bUyrNIFsYclQw5zGUvo53BwoOB7Zmbl91W8Sk4Nkd1stNXanfA1'
        auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
        token_response = requests.post('https://stepik.org/oauth2/token/', data={'grant_type': 'client_credentials'}, auth=auth)
        return token_response.json()['access_token']

    def get_courses_by_tag(self, token):
        courses = []
        headers = {
            'Authorization': f'Bearer {token}'
        }

        page = 0

        while True:
            page += 1

            params = {
                'tag': self.tag_id,
                'page_size': 10,
                'page': page
            }

            response = requests.get(self.url_base + 'courses/', headers=headers, params=params)

            if page == 3:
                break

            courses.extend(response.json()['courses'])

        return courses


    @staticmethod
    def save_course(course_data):
        is_course_exists = Courses.objects.filter(provider_course_id=course_data['id']).exists()
        if is_course_exists:
            return False

        course = Courses(
            title=course_data['title'],
            title_en=course_data.get('title_en', ''),
            provider_course_id=course_data['id'],
            provider=Provider.objects.get(code=1),
            summary=course_data.get('summary', ''),
            cover=course_data.get('cover', ''),
            target_audience=course_data.get('target_audience', ''),
            requirements=course_data.get('requirements', ''),
            description=course_data.get('description', ''),
            total_units=course_data.get('total_units', 0),
            lessons_count=course_data.get('lessons_count', 0),
            quizzes_count=course_data.get('quizzes_count', 0),
            is_paid=course_data.get('is_paid', False),
            price=course_data.get('price', 0),
            currency_code=course_data.get('currency_code', ''),
            is_archived=course_data.get('is_archived', False),
            difficulty=course_data.get('difficulty', Courses.EASY),
            acquired_skills=course_data.get('acquired_skills', ''),
            acquired_assets=course_data.get('acquired_assets', ''),
            learning_format=course_data.get('learning_format', ''),
            course_type=course_data.get('course_type', ''),
            with_certificate=course_data.get('with_certificate', False),
            canonical_url=f"https://stepik.org/course/{course_data['id']}",
            is_active=True
        )
        course.save()
        return course

    def scrap_course_details(self, course, token, section_ids):
        sections = self.get_sections(section_ids, token)
        for section_data in sections:
            section = self.save_section(course, section_data)

        lessons = self.get_lessons(course, token)
        for lesson_data in lessons:
            lesson = self.save_lesson(course, lesson_data)
            units = self.get_units(lesson.provider_lesson_id, token)
            for unit_data in units:
                self.save_unit(lesson, unit_data)
                # assignments = self.get_assignments(unit_data['assignments'], token)
                # for assignment_data in assignments:
                #     assignment = self.save_assignment(unit, lesson, assignment_data)
                #     steps = self.get_steps(assignment.provider_assignment_id, token)
                #     for step_data in steps:
                #         self.save_step(step_data)

    def get_sections(self, section_ids, token):
        sections_data = []
        for section_id in section_ids:
            url = f"https://stepik.org/api/sections/{section_id}/"
            headers = {'Authorization': f'Bearer {token}'}
            response = requests.get(url, headers=headers)
            sections_data.extend(response.json()['sections'])
        return sections_data

    def save_section(self, course, section_data):
        section = Sections(
            provider_lesson_id=section_data['id'],
            course=course,
            position=section_data.get('position', 0),
            description=section_data.get('description', ''),
            title=section_data.get('title', ''),
            is_active=True
        )
        section.save()
        return section

    def get_lessons(self, course, token):
        url = f"https://stepik.org/api/lessons?course={course.provider_course_id}"
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(url, headers=headers)
        return response.json()['lessons']

    def save_lesson(self, course, lesson_data):
        lesson = Lessons(
            provider_lesson_id=lesson_data['id'],
            course=course,
            title=lesson_data.get('title', '')
        )
        lesson.save()
        return lesson

    def get_units(self, lesson_id, token):
        url = f"https://stepik.org/api/units?lesson={lesson_id}"
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(url, headers=headers)
        return response.json()['units']

    def save_unit(self, lesson, unit_data):
        section = Sections.objects.filter(provider_lesson_id=unit_data['section']).first()

        unit = Units(
            provider_unit_id=unit_data['id'],
            lesson=lesson,
            section=section if section else None
        )
        unit.save()
        return unit

    def get_assignments(self, assignment_ids, token):
        assignments = []
        for assignment_id in assignment_ids:
            url = f"https://stepik.org/api/assignments/{assignment_id}/"
            headers = {'Authorization': f'Bearer {token}'}
            response = requests.get(url, headers=headers)
            assignments.append(response.json())
        return assignments

    def save_assignment(self, unit, lesson, assignment_data):
        assignment = Assignments(
            provider_assignment_id=assignment_data['id'],
            unit=unit,
            lesson=lesson
        )
        assignment.save()
        return assignment

    def get_steps(self, assignment_id, token):
        url = f"https://stepik.org/api/steps?assignment={assignment_id}"
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(url, headers=headers)
        return response.json()['steps']

    def save_step(self, step_data):
        step = Steps(
            provider_step_id=step_data['id'],
            position=step_data.get('position', 0),
            block=step_data.get('block', {}),
            is_enabled=step_data.get('is_enabled', True)
        )
        step.save()

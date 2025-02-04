import json
import os

from asgiref.sync import sync_to_async
import asyncio
import logging
from celery import shared_task
import aiohttp
from dotenv import load_dotenv
from bs4 import BeautifulSoup

from .models import *

logger = logging.getLogger(__name__)


class CourseScrapperBase:
    def __init__(self, url: str, provider: str):
        self.provider: str = provider
        self.url_base: str = url

    def _run(self):
        try:
            self.scrap()
            # old_courses = Courses.objects.filter(provider=self.provider)
            # old_courses_links = set(course.canonical_url for course in old_courses)

            # new_courses = self.scrap()   # вызываем метод из подкласса
            # new_courses_dict = {course.canonical_url: course for course in new_courses}
            # new_courses_links = set(course.canonical_url for course in new_courses)
            # added_courses_links = new_courses_links - old_courses_links
            # added_courses = [new_courses_dict[url] for url in added_courses_links]
            # for course in added_courses:
            #     course.save()
        except Exception as e:
            print(e)

    def run_now(self):
        self._run()

    def scrap(self):
        raise NotImplementedError("Method 'scrap' must be implemented in subclasses")


@shared_task
def scrap_now():
    from .scrappers import ALL_SCRAPPERS
    for scrapper in ALL_SCRAPPERS:
        tag = Tags.objects.get(provider_tag_id=scrapper.tag_id)
        print(f"Running {scrapper.provider} {tag.title}")
        scrapper.run_now()


load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID")


@shared_task
def send_courses_to_telegram():
    import asyncio
    asyncio.run(send_courses_to_telegram_async())


def escape_markdown(text):
    escape_chars = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']
    return ''.join(['\\' + char if char in escape_chars else char for char in text])


async def send_courses_to_telegram_async():
    try:
        base_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"

        courses = await sync_to_async(list)(
            Courses.objects.filter(
                is_sent=False,
                is_active=True,
                is_paid=False,
            ).exclude(canonical_url='').order_by('-id')[:1]
        )

        if not courses:
            logger.info("Нет новых курсов для отправки.")
            return

        async with aiohttp.ClientSession() as session:
            for course in courses:
                try:
                    message_parts = [f"📚 <b>{course.title}</b>\n"]
                    if course.summary:
                        message_parts.append(f"📖 <i>{course.summary}</i>\n")
                    if course.target_audience:
                        message_parts.append(f"👤 <b>Для кого:</b> {course.target_audience}\n")
                    if course.requirements:
                        clean_requirements = BeautifulSoup(course.requirements, "html.parser").get_text(separator=" ")
                        message_parts.append(f"⚡ <b>Требования:</b> {clean_requirements}\n")

                    if course.acquired_skills and course.acquired_skills != '[]':
                        try:
                            # Преобразуем строку JSON в список, если это JSON
                            skills = course.acquired_skills.replace("'", '"')
                            skills_list = json.loads(skills)

                            if isinstance(skills_list, list) and skills_list:
                                formatted_skills = "\n".join([f"• {skill}" for skill in skills_list])
                                message_parts.append(f"🎯 <b>Чему научитесь:</b>\n{formatted_skills}\n")
                        except json.JSONDecodeError:
                            logger.warning(f"Ошибка парсинга JSON в acquired_skills для курса {course.title}")

                    if course.is_paid and course.price and course.currency_code:
                        message_parts.append(f"💰 <b>Цена:</b> {course.price} {course.currency_code}\n")
                    message_parts.append("📢 Подпишись на канал, чтобы не пропустить новые курсы!")
                    message = "\n".join(message_parts)

                    params = {
                        'chat_id': TELEGRAM_CHANNEL_ID,
                        'text': message,
                        'parse_mode': 'HTML',
                        "reply_markup": {
                            "inline_keyboard": [
                                [
                                    {
                                        "text": "Перейти на курс",
                                        "url": f"{course.canonical_url}"
                                    }
                                ]
                            ]
                        }
                    }
                    async with session.post(f"{base_url}/sendMessage", json=params) as response:
                        result = await response.json()

                    if response.status == 200 and result.get('ok'):
                        logger.info(f"Message sent successfully: {result}")

                        course.is_sent = True
                        await sync_to_async(course.save)()

                        logger.info(f"Курс '{course.title}' успешно отправлен в Telegram.")
                    else:
                        logger.error(f"Failed to send message: {result}")

                except Exception as e:
                    logger.error(f"Ошибка при отправке курса '{course.title}': {e}")
                    continue

        logger.info(f"Всего отправлено {len(courses)} курсов в Telegram.")

    except Exception as e:
        logger.error(f"Critical error in send_courses_to_telegram: {e}")
        raise

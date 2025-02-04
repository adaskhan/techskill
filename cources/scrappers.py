from .parsers.stepik import StepikCourseScrapper
from .parsers.coursera import CourseraCourseScraper
from .tasks import *

tags = Tags.objects.filter(is_active=True)

ALL_SCRAPPERS = [
    StepikCourseScrapper(tag.provider_tag_id) for tag in tags
]
ALL_SCRAPPERS += [
    CourseraCourseScraper(tag.provider_tag_id) for tag in tags
]
import time
import os
import django
import schedule

# Устанавливаем переменную окружения DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'techskill.settings')

# Инициализируем Django
django.setup()
from cources.tasks import *


schedule.every(1).minutes.do(send_courses_to_telegram)

while True:
    schedule.run_pending()
    time.sleep(1)

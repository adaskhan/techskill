import os
import django


# Устанавливаем переменную окружения DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'techskill.settings')

# Инициализируем Django
django.setup()
from cources.tasks import *

scrap_now()

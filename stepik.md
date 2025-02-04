```markdown
# API Documentation

## Base URL
https://stepik.org/api/
```

## Get courses
```http
GET /courses/ HTTP
```
```json
{
    "meta": {
        "page": 1,
        "has_next": true,
        "has_previous": false
    },
    "courses": [
        {
            "id": 211529,
            "summary": "Наш курс, выполненный в виде интерактивного учебника, поможет освоить основы программирования, чтобы использовать их в дальнейшем в своей профессиональной деятельности. Курс создавался специально для школьников, студентов не инженерных специальностей, людей не из мира IT, и людей, не имеющих опыта в программировании.",
            "workload": "1-2 часа в неделю",
            "cover": "https://cdn.stepik.net/media/cache/images/courses/180595/cover_FmPYMVN/622b2837ca1fa2b905b50e8530f190ed.jpg",
            "intro": "",
            "course_format": "",
            "target_audience": "Курс создавался специально для школьников, студентов не инженерных специальностей, людей не из мира IT, и людей, не имеющих опыта в программировании.",
            "certificate_footer": null,
            "certificate_cover_org": "https://cdn.stepik.net/media/courses/180595/certificate_cover_org_dzCPI2l.jpg",
            "is_certificate_issued": false,
            "is_certificate_auto_issued": true,
            "certificate_regular_threshold": 9,
            "certificate_distinction_threshold": 11,
            "instructors": [
                642349558
            ],
            "certificate": "Stepik",
            "requirements": "<p>Для работы в Google Colab Вам необходимо иметь аккаунт на сервисе Google.com (достаточно иметь почтовый ящик на Gmail.com).</p>",
            "description": "<p>Преимущества интерактивного курса:<br>\n1. Материал хорошо структурирован, – каждая отдельная подтема раскрывается в виде спойлера;<br>\n2. Так как курс создан в ноутбуке колаба (Google Colab), каждый пример можно запустить сразу, находясь прямо внутри темы, которую Вы сейчас проходите;<br>\n3. Материал последовательно изложен (отсутствуют так называемые ссылки «вперед», то есть, ссылки по тексту на не пройденные темы);<br>\n4. В конце каждого урока есть домашнее задание, которое можно выполнять прямо в ноутбуке колаба.</p>",
            "sections": [
                439161
            ],
            "total_units": 11,
            "enrollment": null,
            "is_favorite": false,
            "actions": {
                "view_reports": {
                    "enabled": false,
                    "needs_permission": "teach"
                },
                "edit_reports": {
                    "enabled": false,
                    "needs_permission": "teach"
                },
                "view_grade_book_page": {
                    "enabled": false,
                    "needs_permission": "assist"
                },
                "view_grade_book": {
                    "enabled": false,
                    "needs_permission": "assist"
                },
                "edit_lti": {
                    "enabled": false,
                    "needs_permission": "admin"
                },
                "edit_advanced_settings": {
                    "enabled": false,
                    "needs_permission": "teach"
                },
                "manage_permissions": {
                    "enabled": false,
                    "needs_permission": "admin"
                },
                "view_revenue": {
                    "enabled": false
                },
                "can_be_bought": {
                    "enabled": true
                },
                "can_be_price_changed": {
                    "enabled": false
                },
                "can_be_deleted": {
                    "enabled": false
                },
                "edit_tags": {
                    "enabled": false
                }
            },
            "progress": null,
            "first_lesson": 1401567,
            "first_unit": 1418537,
            "certificate_link": null,
            "certificate_regular_link": null,
            "certificate_distinction_link": null,
            "user_certificate": null,
            "referral_link": null,
            "schedule_link": null,
            "schedule_long_link": null,
            "first_deadline": null,
            "last_deadline": null,
            "subscriptions": [
                "31-78-211529",
                "30-78-211529"
            ],
            "announcements": [],
            "is_contest": false,
            "is_self_paced": true,
            "is_adaptive": false,
            "is_idea_compatible": false,
            "is_in_wishlist": false,
            "last_step": "78-211529",
            "intro_video": {
                "id": 321400,
                "thumbnail": "https://cdn.stepik.net/video/321400/thumbnail/55f8df216a979dd458bdad170de26f4c.jpg",
                "urls": [
                    {
                        "quality": "720",
                        "url": "https://cdn.stepik.net/video/321400/720/40ebb34acb07492a494270c5346e7558.mp4"
                    },
                    {
                        "quality": "540",
                        "url": "https://cdn.stepik.net/video/321400/540/8b81e286ac0419d4e37eb8a82381d520.mp4"
                    },
                    {
                        "quality": "360",
                        "url": "https://cdn.stepik.net/video/321400/360/997c0779ed97f2c3e515bd1bd5055009.mp4"
                    },
                    {
                        "quality": "240",
                        "url": "https://cdn.stepik.net/video/321400/240/10355c9e4ace7bc24204ead6b217a81b.mp4"
                    }
                ],
                "duration": 340,
                "status": "ready",
                "upload_date": "2023-08-02T13:25:36Z",
                "filename": "https://www.youtube.com/watch?v=c9HBGgMx-H0"
            },
            "social_providers": [],
            "authors": [
                642349558
            ],
            "tags": [
                1,
                2,
                3
            ],
            "has_tutors": false,
            "is_enabled": true,
            "is_proctored": false,
            "proctor_url": null,
            "review_summary": 210895,
            "schedule_type": "self_paced",
            "certificates_count": 0,
            "learners_count": 0,
            "lessons_count": 11,
            "quizzes_count": 1,
            "challenges_count": 11,
            "peer_reviews_count": 0,
            "instructor_reviews_count": 0,
            "videos_duration": 7420,
            "time_to_complete": 7422,
            "is_popular": false,
            "is_processed_with_paddle": false,
            "is_unsuitable": false,
            "is_paid": true,
            "price": "2000.00",
            "currency_code": "RUB",
            "display_price": "2000 ₽",
            "default_promo_code_name": null,
            "default_promo_code_price": null,
            "default_promo_code_discount": null,
            "default_promo_code_is_percent_discount": null,
            "default_promo_code_expire_date": null,
            "continue_url": "/course/211529/continue",
            "readiness": 0.8181818181818182,
            "is_archived": false,
            "options": {},
            "price_tier": null,
            "position": 14,
            "is_censored": false,
            "difficulty": "easy",
            "acquired_skills": [
                "1. Вместе мы научимся писать программы на Python в Google Colab;",
                "2. Освоим базовые понятия программирования, такие как условный оператор, функции и циклы;",
                "3. Научимся работать со строками, файлами, списками, словарями и кортежами."
            ],
            "acquired_assets": [
                "1. Навыки, необходимые для написания программ на Python;",
                "2. Благодаря наличию блокнота, возможность отработать теорию на практике на каждом уроке;",
                "3. Сертификат Stepik."
            ],
            "learning_format": "<p>Каждый урок представляет из себя так называемую рабочую тетрадь – блокнот в Google Colab и соответствующее видеопояснение.</p>",
            "content_details": [],
            "issue": null,
            "course_type": "basic_paid",
            "possible_type": null,
            "is_certificate_with_score": false,
            "preview_lesson": null,
            "preview_unit": null,
            "possible_currencies": [],
            "commission_basic": null,
            "commission_promo": null,
            "with_certificate": true,
            "child_courses": [],
            "child_courses_count": 0,
            "parent_courses": [],
            "became_published_at": "2024-08-11T10:10:53.002Z",
            "became_paid_at": "2024-08-11T10:10:53.002Z",
            "title_en": "Basic Python: an interactive course in Google Colab",
            "last_update_price_date": "2024-08-11T09:57:23.686Z",
            "owner": 642349558,
            "language": "ru",
            "is_featured": false,
            "is_public": true,
            "canonical_url": "https://stepik.org/course/211529/",
            "title": "Базовый Python: интерактивный курс в Google Colab",
            "slug": "Базовый-Python-интерактивный-курс-в-Google-Colab-211529",
            "begin_date": "2023-08-03T09:00:00Z",
            "end_date": null,
            "soft_deadline": null,
            "hard_deadline": null,
            "grading_policy": "no_deadlines",
            "begin_date_source": "2023-08-03T09:00:00Z",
            "end_date_source": null,
            "soft_deadline_source": null,
            "hard_deadline_source": null,
            "grading_policy_source": "no_deadlines",
            "is_active": true,
            "create_date": "2024-08-11T09:05:32Z",
            "update_date": "2024-08-11T10:12:52Z",
            "learners_group": null,
            "testers_group": null,
            "moderators_group": null,
            "assistants_group": null,
            "teachers_group": null,
            "admins_group": null,
            "discussions_count": 0,
            "discussion_proxy": null,
            "discussion_threads": [],
            "lti_consumer_key": "",
            "lti_secret_key": "",
            "lti_private_profile": false
        }
    ],
    "enrollments": []
}
```
## Get course 
```http
GET /cources/<pk>/ HTTP
```
```json
{
    "meta": {
        "page": 1,
        "has_next": false,
        "has_previous": false
    },
    "courses": [
        {
            "id": 210731,
            "summary": "Научитесь создавать эффективные запросы для взаимодействия с ChatGPT. Курс включает теоретические знания и практические задания, помогает освоить навыки настройки и оптимизации моделей, а также применение ChatGPT в различных областях. Итоговый проект объединит все полученные знания",
            "workload": "4",
            "cover": "https://cdn.stepik.net/media/cache/images/courses/210731/cover_4ndMufD/fcfde5b8876b9261761d3d10944bb5d7.png",
            "intro": "",
            "course_format": "",
            "target_audience": "Разработчики, стремящиеся освоить работу с ChatGPT\nПреподаватели и образовательные специалисты, желающие внедрить AI в учебный процесс\nБизнес-аналитики и маркетологи, ищущие новые инструменты для работы с клиентами и создания контента\nЛюбой, кто интересуется искусственным интеллектом и его применениями\n",
            "certificate_footer": null,
            "certificate_cover_org": null,
            "is_certificate_issued": false,
            "is_certificate_auto_issued": false,
            "certificate_regular_threshold": null,
            "certificate_distinction_threshold": null,
            "instructors": [
                889023332
            ],
            "certificate": "",
            "requirements": "<ul>\n\t<li>Базовые знания в области программирования</li>\n\t<li>Желание изучать и экспериментировать с новыми технологиями</li>\n\t<li>Доступ к интернету</li>\n</ul>",
            "description": "<p>Этот курс научит вас искусству создания эффективных запросов для ChatGPT. Вы узнаете, как работать с языковой моделью, оптимизировать ее параметры и применять ChatGPT в различных областях. Курс включает теоретические знания и практические задания, помогая вам освоить все необходимые навыки для создания специализированных приложений и использования ChatGPT в реальных проектах. По окончании курса вы выполните итоговый проект, который объединит все полученные знания и навыки.</p>",
            "sections": [
                436368,
                436369,
                436370,
                436371,
                436372,
                436373
            ],
            "total_units": 12,
            "enrollment": null,
            "is_favorite": false,
            "actions": {
                "view_reports": {
                    "enabled": false,
                    "needs_permission": "teach"
                },
                "edit_reports": {
                    "enabled": false,
                    "needs_permission": "teach"
                },
                "view_grade_book_page": {
                    "enabled": false,
                    "needs_permission": "assist"
                },
                "view_grade_book": {
                    "enabled": false,
                    "needs_permission": "assist"
                },
                "edit_lti": {
                    "enabled": false,
                    "needs_permission": "admin"
                },
                "edit_advanced_settings": {
                    "enabled": false,
                    "needs_permission": "teach"
                },
                "manage_permissions": {
                    "enabled": false,
                    "needs_permission": "admin"
                },
                "view_revenue": {
                    "enabled": false
                },
                "can_be_bought": {
                    "enabled": false
                },
                "can_be_price_changed": {
                    "enabled": true
                },
                "can_be_deleted": {
                    "enabled": false
                },
                "edit_tags": {
                    "enabled": false
                }
            },
            "progress": null,
            "first_lesson": 1391178,
            "first_unit": 1407907,
            "certificate_link": null,
            "certificate_regular_link": null,
            "certificate_distinction_link": null,
            "user_certificate": null,
            "referral_link": null,
            "schedule_link": null,
            "schedule_long_link": null,
            "first_deadline": null,
            "last_deadline": null,
            "subscriptions": [
                "31-78-210731",
                "30-78-210731"
            ],
            "announcements": [],
            "is_contest": false,
            "is_self_paced": true,
            "is_adaptive": false,
            "is_idea_compatible": false,
            "is_in_wishlist": false,
            "last_step": "78-210731",
            "intro_video": null,
            "social_providers": [],
            "authors": [
                889023332
            ],
            "tags": [
                1,
                2,
                3,
                42,
                113,
                348,
                365,
                367
            ],
            "has_tutors": false,
            "is_enabled": true,
            "is_proctored": false,
            "proctor_url": null,
            "review_summary": 210097,
            "schedule_type": "self_paced",
            "certificates_count": 0,
            "learners_count": 1,
            "lessons_count": 12,
            "quizzes_count": 24,
            "challenges_count": 0,
            "peer_reviews_count": 0,
            "instructor_reviews_count": 0,
            "videos_duration": 0,
            "time_to_complete": null,
            "is_popular": false,
            "is_processed_with_paddle": false,
            "is_unsuitable": false,
            "is_paid": false,
            "price": null,
            "currency_code": null,
            "display_price": "-",
            "default_promo_code_name": null,
            "default_promo_code_price": null,
            "default_promo_code_discount": null,
            "default_promo_code_is_percent_discount": null,
            "default_promo_code_expire_date": null,
            "continue_url": "/course/210731/continue",
            "readiness": 0.9090909090909091,
            "is_archived": false,
            "options": {},
            "price_tier": null,
            "position": 1,
            "is_censored": false,
            "difficulty": "easy",
            "acquired_skills": [
                "Применять техники создания эффективных запросов (prompts)",
                "Настраивать и оптимизировать параметры моделей GPT",
                "Использовать ChatGPT в образовании, бизнесе и маркетинге",
                "Разрабатывать и внедрять специализированные приложения с использованием ChatGPT"
            ],
            "acquired_assets": [
                "Навыки и знания, востребованные работодателем",
                "Возможность отработать теорию на практике",
                "Доступ к форуму решений",
                "Проекты в портфолио"
            ],
            "learning_format": "<ul>\n\t<li>Теоретические и практические модули</li>\n\t<li>Обучение через текстовые материалы и практические задания</li>\n\t<li>Итоговый проект для применения всех полученных знаний</li>\n</ul>",
            "content_details": [],
            "issue": null,
            "course_type": "basic",
            "possible_type": null,
            "is_certificate_with_score": false,
            "preview_lesson": null,
            "preview_unit": null,
            "possible_currencies": [],
            "commission_basic": null,
            "commission_promo": null,
            "with_certificate": false,
            "child_courses": [],
            "child_courses_count": 0,
            "parent_courses": [],
            "became_published_at": "2024-08-06T11:25:57.196Z",
            "became_paid_at": null,
            "title_en": "Prompt Engineering for ChatGPT",
            "last_update_price_date": null,
            "owner": 889023332,
            "language": "ru",
            "is_featured": false,
            "is_public": true,
            "canonical_url": "https://stepik.org/course/210731/",
            "title": "Prompt Engineering for ChatGPT",
            "slug": "Prompt-Engineering-for-ChatGPT-210731",
            "begin_date": "2024-07-05T07:00:00Z",
            "end_date": null,
            "soft_deadline": null,
            "hard_deadline": null,
            "grading_policy": "no_deadlines",
            "begin_date_source": "2024-07-05T07:00:00Z",
            "end_date_source": null,
            "soft_deadline_source": null,
            "hard_deadline_source": null,
            "grading_policy_source": "no_deadlines",
            "is_active": true,
            "create_date": "2024-07-28T15:15:22Z",
            "update_date": "2024-08-06T11:25:57Z",
            "learners_group": null,
            "testers_group": null,
            "moderators_group": null,
            "assistants_group": null,
            "teachers_group": null,
            "admins_group": null,
            "discussions_count": 0,
            "discussion_proxy": null,
            "discussion_threads": [],
            "lti_consumer_key": "",
            "lti_secret_key": "",
            "lti_private_profile": false
        }
    ],
    "enrollments": []
}
```
## Get section
```http
GET /sections/<pk>/ HTTP
```
```json
{
    "meta": {
        "page": 1,
        "has_next": false,
        "has_previous": false
    },
    "sections": [
        {
            "id": 436368,
            "course": 210731,
            "units": [
                1407907,
                1407889,
                1407890
            ],
            "position": 1,
            "discounting_policy": "no_discount",
            "progress": "79-436368",
            "actions": {},
            "required_section": null,
            "required_percent": 100,
            "is_requirement_satisfied": true,
            "is_exam": false,
            "is_exam_without_progress": false,
            "is_random_exam": false,
            "exam_duration_minutes": 120,
            "random_exam_problems_course": null,
            "random_exam_problems_count": 20,
            "exam_session": null,
            "proctor_session": null,
            "description": "Этот модуль познакомит вас с основами Prompt Engineering на основе ChatGPT. Вы узнаете, что такое ChatGPT, как он работает, и получите первые навыки работы с этой моделью",
            "is_proctoring_can_be_scheduled": false,
            "title": "Введение в Prompt Engineering",
            "slug": "Введение-в-Prompt-Engineering-436368",
            "begin_date": "2024-08-01T07:00:00Z",
            "end_date": null,
            "soft_deadline": null,
            "hard_deadline": null,
            "grading_policy": "no_deadlines",
            "begin_date_source": "2024-08-01T07:00:00Z",
            "end_date_source": null,
            "soft_deadline_source": null,
            "hard_deadline_source": null,
            "grading_policy_source": null,
            "is_active": true,
            "create_date": "2024-07-28T15:30:22Z",
            "update_date": "2024-07-29T10:46:25Z"
        }
    ]
}
```
## Get lessons
```http
GET /lessons/ HTTP
```
```json
{
    "meta": {
        "page": 1,
        "has_next": false,
        "has_previous": false
    },
    "lessons": [
        {
            "id": 1391160,
            "steps": [
                5769969,
                5770159,
                5771664,
                5770157,
                5770158,
                5770160
            ],
            "actions": {
                "learn_lesson": "#"
            },
            "progress": "76-1391160",
            "subscriptions": [
                "31-76-1391160",
                "30-76-1391160"
            ],
            "viewed_by": 1,
            "passed_by": 1,
            "time_to_complete": null,
            "cover_url": null,
            "is_comments_enabled": true,
            "is_exam_without_progress": false,
            "is_blank": false,
            "is_draft": false,
            "is_orphaned": false,
            "courses": [
                210731
            ],
            "units": [
                1407889
            ],
            "owner": 889023332,
            "language": "ru",
            "is_featured": false,
            "is_public": true,
            "canonical_url": "https://stepik.org/lesson/1391160/",
            "title": "Урок 2: Структура и формулирование запросов",
            "slug": "Урок-2-Структура-и-формулирование-запросов-1391160",
            "create_date": "2024-07-28T15:30:27Z",
            "update_date": "2024-07-29T10:03:06Z",
            "learners_group": null,
            "testers_group": null,
            "moderators_group": null,
            "assistants_group": null,
            "teachers_group": null,
            "admins_group": null,
            "discussions_count": 0,
            "discussion_proxy": "76-1391160-1",
            "discussion_threads": [
                "76-1391160-1"
            ],
            "epic_count": 0,
            "abuse_count": 0,
            "vote_delta": 0,
            "vote": "76-1391160",
            "lti_consumer_key": "",
            "lti_secret_key": "",
            "lti_private_profile": false
        },
        {
            "id": 1391161,
            "steps": [
                5769971,
                5771665,
                5770186,
                5770185,
                5770192
            ],
            "actions": {
                "learn_lesson": "#"
            },
            "progress": "76-1391161",
            "subscriptions": [
                "31-76-1391161",
                "30-76-1391161"
            ],
            "viewed_by": 1,
            "passed_by": 1,
            "time_to_complete": null,
            "cover_url": null,
            "is_comments_enabled": true,
            "is_exam_without_progress": false,
            "is_blank": false,
            "is_draft": false,
            "is_orphaned": false,
            "courses": [
                210731
            ],
            "units": [
                1407890
            ],
            "owner": 889023332,
            "language": "ru",
            "is_featured": false,
            "is_public": true,
            "canonical_url": "https://stepik.org/lesson/1391161/",
            "title": "Урок 3: Использование параметров и ограничений",
            "slug": "Урок-3-Использование-параметров-и-ограничений-1391161",
            "create_date": "2024-07-28T15:30:30Z",
            "update_date": "2024-07-29T10:28:34Z",
            "learners_group": null,
            "testers_group": null,
            "moderators_group": null,
            "assistants_group": null,
            "teachers_group": null,
            "admins_group": null,
            "discussions_count": 0,
            "discussion_proxy": "76-1391161-1",
            "discussion_threads": [
                "76-1391161-1"
            ],
            "epic_count": 0,
            "abuse_count": 0,
            "vote_delta": 0,
            "vote": "76-1391161",
            "lti_consumer_key": "",
            "lti_secret_key": "",
            "lti_private_profile": false
        },
        {
            "id": 1391162,
            "steps": [],
            "actions": {},
            "progress": null,
            "subscriptions": [
                "31-76-1391162",
                "30-76-1391162"
            ],
            "viewed_by": 1,
            "passed_by": 1,
            "time_to_complete": null,
            "cover_url": null,
            "is_comments_enabled": true,
            "is_exam_without_progress": false,
            "is_blank": false,
            "is_draft": false,
            "is_orphaned": false,
            "courses": [
                210731
            ],
            "units": [
                1407891
            ],
            "owner": 889023332,
            "language": "ru",
            "is_featured": false,
            "is_public": false,
            "canonical_url": "https://stepik.org/lesson/1391162/",
            "title": "Урок 4: Создание диалогов и поддержка контекста",
            "slug": "Урок-4-Создание-диалогов-и-поддержка-контекста-1391162",
            "create_date": "2024-07-28T15:30:33Z",
            "update_date": "2024-07-29T10:29:49Z",
            "learners_group": null,
            "testers_group": null,
            "moderators_group": null,
            "assistants_group": null,
            "teachers_group": null,
            "admins_group": null,
            "discussions_count": 0,
            "discussion_proxy": null,
            "discussion_threads": [],
            "epic_count": 0,
            "abuse_count": 0,
            "vote_delta": 0,
            "vote": null,
            "lti_consumer_key": "",
            "lti_secret_key": "",
            "lti_private_profile": false
        },
        {
            "id": 1391163,
            "steps": [],
            "actions": {},
            "progress": null,
            "subscriptions": [
                "31-76-1391163",
                "30-76-1391163"
            ],
            "viewed_by": 1,
            "passed_by": 1,
            "time_to_complete": null,
            "cover_url": null,
            "is_comments_enabled": true,
            "is_exam_without_progress": false,
            "is_blank": false,
            "is_draft": false,
            "is_orphaned": false,
            "courses": [
                210731
            ],
            "units": [
                1407892
            ],
            "owner": 889023332,
            "language": "ru",
            "is_featured": false,
            "is_public": false,
            "canonical_url": "https://stepik.org/lesson/1391163/",
            "title": "Урок 5: Генерация креативного контента",
            "slug": "Урок-5-Генерация-креативного-контента-1391163",
            "create_date": "2024-07-28T15:30:35Z",
            "update_date": "2024-07-29T09:02:16Z",
            "learners_group": null,
            "testers_group": null,
            "moderators_group": null,
            "assistants_group": null,
            "teachers_group": null,
            "admins_group": null,
            "discussions_count": 0,
            "discussion_proxy": null,
            "discussion_threads": [],
            "epic_count": 0,
            "abuse_count": 0,
            "vote_delta": 0,
            "vote": null,
            "lti_consumer_key": "",
            "lti_secret_key": "",
            "lti_private_profile": false
        },
        {
            "id": 1391164,
            "steps": [],
            "actions": {},
            "progress": null,
            "subscriptions": [
                "31-76-1391164",
                "30-76-1391164"
            ],
            "viewed_by": 1,
            "passed_by": 1,
            "time_to_complete": null,
            "cover_url": null,
            "is_comments_enabled": true,
            "is_exam_without_progress": false,
            "is_blank": false,
            "is_draft": false,
            "is_orphaned": false,
            "courses": [
                210731
            ],
            "units": [
                1407893
            ],
            "owner": 889023332,
            "language": "ru",
            "is_featured": false,
            "is_public": false,
            "canonical_url": "https://stepik.org/lesson/1391164/",
            "title": "Урок 6: Интеграция ChatGPT в приложения",
            "slug": "Урок-6-Интеграция-ChatGPT-в-приложения-1391164",
            "create_date": "2024-07-28T15:30:42Z",
            "update_date": "2024-07-29T09:58:20Z",
            "learners_group": null,
            "testers_group": null,
            "moderators_group": null,
            "assistants_group": null,
            "teachers_group": null,
            "admins_group": null,
            "discussions_count": 0,
            "discussion_proxy": null,
            "discussion_threads": [],
            "epic_count": 0,
            "abuse_count": 0,
            "vote_delta": 0,
            "vote": null,
            "lti_consumer_key": "",
            "lti_secret_key": "",
            "lti_private_profile": false
        },
        {
            "id": 1391165,
            "steps": [],
            "actions": {},
            "progress": null,
            "subscriptions": [
                "31-76-1391165",
                "30-76-1391165"
            ],
            "viewed_by": 1,
            "passed_by": 1,
            "time_to_complete": null,
            "cover_url": null,
            "is_comments_enabled": true,
            "is_exam_without_progress": false,
            "is_blank": false,
            "is_draft": false,
            "is_orphaned": false,
            "courses": [
                210731
            ],
            "units": [
                1407894
            ],
            "owner": 889023332,
            "language": "ru",
            "is_featured": false,
            "is_public": false,
            "canonical_url": "https://stepik.org/lesson/1391165/",
            "title": "Урок 7: Этические аспекты и ограничения",
            "slug": "Урок-7-Этические-аспекты-и-ограничения-1391165",
            "create_date": "2024-07-28T15:30:44Z",
            "update_date": "2024-07-29T10:31:21Z",
            "learners_group": null,
            "testers_group": null,
            "moderators_group": null,
            "assistants_group": null,
            "teachers_group": null,
            "admins_group": null,
            "discussions_count": 0,
            "discussion_proxy": null,
            "discussion_threads": [],
            "epic_count": 0,
            "abuse_count": 0,
            "vote_delta": 0,
            "vote": null,
            "lti_consumer_key": "",
            "lti_secret_key": "",
            "lti_private_profile": false
        },
        {
            "id": 1391166,
            "steps": [],
            "actions": {},
            "progress": null,
            "subscriptions": [
                "31-76-1391166",
                "30-76-1391166"
            ],
            "viewed_by": 1,
            "passed_by": 1,
            "time_to_complete": null,
            "cover_url": null,
            "is_comments_enabled": true,
            "is_exam_without_progress": false,
            "is_blank": false,
            "is_draft": false,
            "is_orphaned": false,
            "courses": [
                210731
            ],
            "units": [
                1407895
            ],
            "owner": 889023332,
            "language": "ru",
            "is_featured": false,
            "is_public": false,
            "canonical_url": "https://stepik.org/lesson/1391166/",
            "title": "Урок 8: Использование ChatGPT в образовании",
            "slug": "Урок-8-Использование-ChatGPT-в-образовании-1391166",
            "create_date": "2024-07-28T15:30:47Z",
            "update_date": "2024-07-29T09:59:54Z",
            "learners_group": null,
            "testers_group": null,
            "moderators_group": null,
            "assistants_group": null,
            "teachers_group": null,
            "admins_group": null,
            "discussions_count": 0,
            "discussion_proxy": null,
            "discussion_threads": [],
            "epic_count": 0,
            "abuse_count": 0,
            "vote_delta": 0,
            "vote": null,
            "lti_consumer_key": "",
            "lti_secret_key": "",
            "lti_private_profile": false
        },
        {
            "id": 1391167,
            "steps": [],
            "actions": {},
            "progress": null,
            "subscriptions": [
                "31-76-1391167",
                "30-76-1391167"
            ],
            "viewed_by": 1,
            "passed_by": 1,
            "time_to_complete": null,
            "cover_url": null,
            "is_comments_enabled": true,
            "is_exam_without_progress": false,
            "is_blank": false,
            "is_draft": false,
            "is_orphaned": false,
            "courses": [
                210731
            ],
            "units": [
                1407896
            ],
            "owner": 889023332,
            "language": "ru",
            "is_featured": false,
            "is_public": false,
            "canonical_url": "https://stepik.org/lesson/1391167/",
            "title": "Урок 9: ChatGPT в бизнесе и маркетинге",
            "slug": "Урок-9-ChatGPT-в-бизнесе-и-маркетинге-1391167",
            "create_date": "2024-07-28T15:30:49Z",
            "update_date": "2024-07-29T10:00:41Z",
            "learners_group": null,
            "testers_group": null,
            "moderators_group": null,
            "assistants_group": null,
            "teachers_group": null,
            "admins_group": null,
            "discussions_count": 0,
            "discussion_proxy": null,
            "discussion_threads": [],
            "epic_count": 0,
            "abuse_count": 0,
            "vote_delta": 0,
            "vote": null,
            "lti_consumer_key": "",
            "lti_secret_key": "",
            "lti_private_profile": false
        },
        {
            "id": 1391168,
            "steps": [],
            "actions": {},
            "progress": null,
            "subscriptions": [
                "31-76-1391168",
                "30-76-1391168"
            ],
            "viewed_by": 1,
            "passed_by": 1,
            "time_to_complete": null,
            "cover_url": null,
            "is_comments_enabled": true,
            "is_exam_without_progress": false,
            "is_blank": false,
            "is_draft": false,
            "is_orphaned": false,
            "courses": [
                210731
            ],
            "units": [
                1407897
            ],
            "owner": 889023332,
            "language": "ru",
            "is_featured": false,
            "is_public": false,
            "canonical_url": "https://stepik.org/lesson/1391168/",
            "title": "Урок 10: Настройка моделей GPT",
            "slug": "Урок-10-Настройка-моделей-GPT-1391168",
            "create_date": "2024-07-28T15:30:51Z",
            "update_date": "2024-07-29T10:36:42Z",
            "learners_group": null,
            "testers_group": null,
            "moderators_group": null,
            "assistants_group": null,
            "teachers_group": null,
            "admins_group": null,
            "discussions_count": 0,
            "discussion_proxy": null,
            "discussion_threads": [],
            "epic_count": 0,
            "abuse_count": 0,
            "vote_delta": 0,
            "vote": null,
            "lti_consumer_key": "",
            "lti_secret_key": "",
            "lti_private_profile": false
        },
        {
            "id": 1391170,
            "steps": [],
            "actions": {},
            "progress": null,
            "subscriptions": [
                "31-76-1391170",
                "30-76-1391170"
            ],
            "viewed_by": 1,
            "passed_by": 1,
            "time_to_complete": null,
            "cover_url": null,
            "is_comments_enabled": true,
            "is_exam_without_progress": false,
            "is_blank": false,
            "is_draft": false,
            "is_orphaned": false,
            "courses": [
                210731
            ],
            "units": [
                1407898
            ],
            "owner": 889023332,
            "language": "ru",
            "is_featured": false,
            "is_public": false,
            "canonical_url": "https://stepik.org/lesson/1391170/",
            "title": "Урок 11: Оптимизация производительности ChatGPT",
            "slug": "Урок-11-Оптимизация-производительности-ChatGPT-1391170",
            "create_date": "2024-07-28T15:33:21Z",
            "update_date": "2024-07-29T10:36:30Z",
            "learners_group": null,
            "testers_group": null,
            "moderators_group": null,
            "assistants_group": null,
            "teachers_group": null,
            "admins_group": null,
            "discussions_count": 0,
            "discussion_proxy": null,
            "discussion_threads": [],
            "epic_count": 0,
            "abuse_count": 0,
            "vote_delta": 0,
            "vote": null,
            "lti_consumer_key": "",
            "lti_secret_key": "",
            "lti_private_profile": false
        },
        {
            "id": 1391171,
            "steps": [],
            "actions": {},
            "progress": null,
            "subscriptions": [
                "31-76-1391171",
                "30-76-1391171"
            ],
            "viewed_by": 1,
            "passed_by": 0,
            "time_to_complete": null,
            "cover_url": null,
            "is_comments_enabled": true,
            "is_exam_without_progress": false,
            "is_blank": false,
            "is_draft": false,
            "is_orphaned": false,
            "courses": [
                210731
            ],
            "units": [
                1407899
            ],
            "owner": 889023332,
            "language": "ru",
            "is_featured": false,
            "is_public": false,
            "canonical_url": "https://stepik.org/lesson/1391171/",
            "title": "Урок 12: Итоговый проект",
            "slug": "Урок-12-Итоговый-проект-1391171",
            "create_date": "2024-07-28T15:33:23Z",
            "update_date": "2024-07-29T10:37:57Z",
            "learners_group": null,
            "testers_group": null,
            "moderators_group": null,
            "assistants_group": null,
            "teachers_group": null,
            "admins_group": null,
            "discussions_count": 0,
            "discussion_proxy": null,
            "discussion_threads": [],
            "epic_count": 0,
            "abuse_count": 0,
            "vote_delta": 0,
            "vote": null,
            "lti_consumer_key": "",
            "lti_secret_key": "",
            "lti_private_profile": false
        },
        {
            "id": 1391178,
            "steps": [
                5770113,
                5771634,
                5770136,
                5770137,
                5770144
            ],
            "actions": {
                "learn_lesson": "#"
            },
            "progress": "76-1391178",
            "subscriptions": [
                "31-76-1391178",
                "30-76-1391178"
            ],
            "viewed_by": 2,
            "passed_by": 1,
            "time_to_complete": null,
            "cover_url": null,
            "is_comments_enabled": true,
            "is_exam_without_progress": false,
            "is_blank": false,
            "is_draft": false,
            "is_orphaned": false,
            "courses": [
                210731
            ],
            "units": [
                1407907
            ],
            "owner": 889023332,
            "language": "ru",
            "is_featured": false,
            "is_public": true,
            "canonical_url": "https://stepik.org/lesson/1391178/",
            "title": "Урок 1: Знакомство с ChatGPT",
            "slug": "Урок-1-Знакомство-с-ChatGPT-1391178",
            "create_date": "2024-07-28T15:55:00Z",
            "update_date": "2024-07-29T08:54:11Z",
            "learners_group": null,
            "epic_count": 0,
            "abuse_count": 0,
            "vote_delta": 0,
            "vote": "76-1391178",
            "lti_consumer_key": "",
            "lti_secret_key": "",
            "lti_private_profile": false
        }
    ]
}
```
## Get lesson
```http
GET /lessons/<pk>/ HTTP
```
```json
{
    "meta": {
        "page": 1,
        "has_next": false,
        "has_previous": false
    },
    "lessons": [
        {
            "id": 1391178,
            "steps": [
                5770113,
                5771634,
                5770136,
                5770137,
                5770144
            ],
            "actions": {
                "learn_lesson": "#"
            },
            "progress": "76-1391178",
            "subscriptions": [
                "31-76-1391178",
                "30-76-1391178"
            ],
            "viewed_by": 2,
            "passed_by": 1,
            "time_to_complete": null,
            "cover_url": null,
            "is_comments_enabled": true,
            "is_exam_without_progress": false,
            "is_blank": false,
            "is_draft": false,
            "is_orphaned": false,
            "courses": [
                210731
            ],
            "units": [
                1407907
            ],
            "owner": 889023332,
            "language": "ru",
            "is_featured": false,
            "is_public": true,
            "canonical_url": "https://stepik.org/lesson/1391178/",
            "title": "Урок 1: Знакомство с ChatGPT",
            "slug": "Урок-1-Знакомство-с-ChatGPT-1391178",
            "create_date": "2024-07-28T15:55:00Z",
            "update_date": "2024-07-29T08:54:11Z",
            "learners_group": null,
            "testers_group": null,
            "moderators_group": null,
            "assistants_group": null,
            "teachers_group": null,
            "admins_group": null,
            "discussions_count": 0,
            "discussion_proxy": "76-1391178-1",
            "discussion_threads": [
                "76-1391178-1"
            ],
            "epic_count": 0,
            "abuse_count": 0,
            "vote_delta": 0,
            "vote": "76-1391178",
            "lti_consumer_key": "",
            "lti_secret_key": "",
            "lti_private_profile": false
        }
    ]
}
```
## Get units
```http
GET /units/ HTTP
```
```json
{
    "meta": {
        "page": 1,
        "has_next": false,
        "has_previous": false
    },
    "units": [
        {
            "id": 1407907,
            "section": 436368,
            "lesson": 1391178,
            "assignments": [
                5819607,
                5819632,
                5819633,
                5819634,
                5821132
            ],
            "position": 1,
            "actions": {},
            "progress": null,
            "begin_date": "2024-08-01T07:00:00Z",
            "end_date": null,
            "soft_deadline": null,
            "hard_deadline": null,
            "grading_policy": "no_deadlines",
            "begin_date_source": null,
            "end_date_source": null,
            "soft_deadline_source": null,
            "hard_deadline_source": null,
            "grading_policy_source": null,
            "is_active": true,
            "create_date": "2024-07-28T15:55:00Z",
            "update_date": "2024-07-29T08:54:11Z"
        },
        {
            "id": 1407889,
            "section": 436368,
            "lesson": 1391160,
            "assignments": [
                5819460,
                5819652,
                5819653,
                5819651,
                5819654,
                5821162
            ],
            "position": 2,
            "actions": {},
            "progress": null,
            "begin_date": "2024-08-01T07:00:00Z",
            "end_date": null,
            "soft_deadline": null,
            "hard_deadline": null,
            "grading_policy": "no_deadlines",
            "begin_date_source": null,
            "end_date_source": null,
            "soft_deadline_source": null,
            "hard_deadline_source": null,
            "grading_policy_source": null,
            "is_active": true,
            "create_date": "2024-07-28T15:30:28Z",
            "update_date": "2024-07-29T10:03:06Z"
        },
        {
            "id": 1407890,
            "section": 436368,
            "lesson": 1391161,
            "assignments": [
                5819461,
                5819681,
                5819680,
                5819686,
                5821163
            ],
            "position": 3,
            "actions": {},
            "progress": null,
            "begin_date": "2024-08-01T07:00:00Z",
            "end_date": null,
            "soft_deadline": null,
            "hard_deadline": null,
            "grading_policy": "no_deadlines",
            "begin_date_source": null,
            "end_date_source": null,
            "soft_deadline_source": null,
            "hard_deadline_source": null,
            "grading_policy_source": null,
            "is_active": true,
            "create_date": "2024-07-28T15:30:31Z",
            "update_date": "2024-07-29T10:28:34Z"
        },
        {
            "id": 1407891,
            "section": 436369,
            "lesson": 1391162,
            "assignments": [
                5819462,
                5820662,
                5820661,
                5821277
            ],
            "position": 1,
            "actions": {},
            "progress": null,
            "begin_date": "2024-08-02T07:00:00Z",
            "end_date": null,
            "soft_deadline": null,
            "hard_deadline": null,
            "grading_policy": "no_deadlines",
            "begin_date_source": null,
            "end_date_source": null,
            "soft_deadline_source": null,
            "hard_deadline_source": null,
            "grading_policy_source": null,
            "is_active": true,
            "create_date": "2024-07-28T15:30:34Z",
            "update_date": "2024-07-29T10:29:49Z"
        },
        {
            "id": 1407892,
            "section": 436369,
            "lesson": 1391163,
            "assignments": [
                5819463,
                5820666,
                5820665,
                5820664,
                5821279
            ],
            "position": 2,
            "actions": {},
            "progress": null,
            "begin_date": "2024-08-02T07:00:00Z",
            "end_date": null,
            "soft_deadline": null,
            "hard_deadline": null,
            "grading_policy": "no_deadlines",
            "begin_date_source": null,
            "end_date_source": null,
            "soft_deadline_source": null,
            "hard_deadline_source": null,
            "grading_policy_source": null,
            "is_active": true,
            "create_date": "2024-07-28T15:30:36Z",
            "update_date": "2024-07-29T09:03:16Z"
        },
        {
            "id": 1407893,
            "section": 436370,
            "lesson": 1391164,
            "assignments": [
                5819464,
                5820671,
                5820673,
                5820672,
                5821282
            ],
            "position": 1,
            "actions": {},
            "progress": null,
            "begin_date": "2024-08-03T07:00:00Z",
            "end_date": null,
            "soft_deadline": null,
            "hard_deadline": null,
            "grading_policy": "no_deadlines",
            "begin_date_source": null,
            "end_date_source": null,
            "soft_deadline_source": null,
            "hard_deadline_source": null,
            "grading_policy_source": null,
            "is_active": true,
            "create_date": "2024-07-28T15:30:43Z",
            "update_date": "2024-07-29T09:58:20Z"
        },
        {
            "id": 1407894,
            "section": 436370,
            "lesson": 1391165,
            "assignments": [
                5819465,
                5821063,
                5821061,
                5821062,
                5821291
            ],
            "position": 2,
            "actions": {},
            "progress": null,
            "begin_date": "2024-08-03T07:00:00Z",
            "end_date": null,
            "soft_deadline": null,
            "hard_deadline": null,
            "grading_policy": "no_deadlines",
            "begin_date_source": null,
            "end_date_source": null,
            "soft_deadline_source": null,
            "hard_deadline_source": null,
            "grading_policy_source": null,
            "is_active": true,
            "create_date": "2024-07-28T15:30:45Z",
            "update_date": "2024-07-29T10:31:21Z"
        },
        {
            "id": 1407895,
            "section": 436371,
            "lesson": 1391166,
            "assignments": [
                5819466,
                5821084,
                5821455,
                5821456
            ],
            "position": 1,
            "actions": {},
            "progress": null,
            "begin_date": "2024-08-04T07:00:00Z",
            "end_date": null,
            "soft_deadline": null,
            "hard_deadline": null,
            "grading_policy": "no_deadlines",
            "begin_date_source": null,
            "end_date_source": null,
            "soft_deadline_source": null,
            "hard_deadline_source": null,
            "grading_policy_source": null,
            "is_active": true,
            "create_date": "2024-07-28T15:30:47Z",
            "update_date": "2024-07-29T10:00:54Z"
        },
        {
            "id": 1407896,
            "section": 436371,
            "lesson": 1391167,
            "assignments": [
                5819467,
                5821093,
                5821092,
                5821094,
                5821095
            ],
            "position": 2,
            "actions": {},
            "progress": null,
            "begin_date": "2024-08-04T07:00:00Z",
            "end_date": null,
            "soft_deadline": null,
            "hard_deadline": null,
            "grading_policy": "no_deadlines",
            "begin_date_source": null,
            "end_date_source": null,
            "soft_deadline_source": null,
            "hard_deadline_source": null,
            "grading_policy_source": null,
            "is_active": true,
            "create_date": "2024-07-28T15:30:49Z",
            "update_date": "2024-07-29T10:00:41Z"
        },
        {
            "id": 1407897,
            "section": 436372,
            "lesson": 1391168,
            "assignments": [
                5819468,
                5821097,
                5821109,
                5821108
            ],
            "position": 1,
            "actions": {},
            "progress": null,
            "begin_date": "2024-08-05T07:00:00Z",
            "end_date": null,
            "soft_deadline": null,
            "hard_deadline": null,
            "grading_policy": "no_deadlines",
            "begin_date_source": null,
            "end_date_source": null,
            "soft_deadline_source": null,
            "hard_deadline_source": null,
            "grading_policy_source": null,
            "is_active": true,
            "create_date": "2024-07-28T15:30:52Z",
            "update_date": "2024-07-29T10:36:42Z"
        }
    ]
}
```
## Get steps
```http
GET /steps/ HTTP
```
```json
{
    "meta": {
        "page": 1,
        "has_next": false,
        "has_previous": false
    },
    "steps": [
        {
            "id": 5770113,
            "lesson": 1391178,
            "position": 1,
            "status": "ready",
            "block": {
                "name": "text",
                "text": "<p>ChatGPT — это языковая модель¹, разработанная компанией OpenAI. Она основана на архитектуре GPT (Generative Pre-trained Transformer), которая предназначена для понимания и генерации текста на естественном языке. ChatGPT может использоваться для разнообразных задач, таких как написание текстов, ответ на вопросы, создание диалогов и многое другое.</p>\n\n<p><strong>Пример использования ChatGPT:</strong></p>\n\n<p> </p>\n\n<p><code>Пользователь: Привет, как дела? ChatGPT: </code></p>\n\n<p><code>Привет! Я работаю отлично, спасибо. Чем могу помочь?</code></p>",
                "video": null,
                "options": {},
                "subtitle_files": [],
                "is_deprecated": false
            },
            "actions": {
                "comment": "#"
            },
            "progress": "77-5770113",
            "subscriptions": [
                "31-77-5770113",
                "30-77-5770113"
            ],
            "instruction": null,
            "session": null,
            "instruction_type": null,
            "viewed_by": 2,
            "passed_by": 2,
            "correct_ratio": null,
            "worth": 0,
            "is_solutions_unlocked": false,
            "solutions_unlocked_attempts": 3,
            "has_submissions_restrictions": false,
            "max_submissions_count": 3,
            "variation": 1,
            "variations_count": 1,
            "is_enabled": true,
            "needs_plan": null,
            "create_date": "2024-07-28T15:55:01Z",
            "update_date": "2024-07-29T08:40:13Z",
            "discussions_count": 0,
            "discussion_proxy": "77-5770113-1",
            "discussion_threads": [
                "77-5770113-1"
            ]
        }
    ]
}
```
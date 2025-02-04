from email.policy import default

from django.db import models


class Provider(models.Model):
    name = models.CharField(verbose_name="название провайдера", max_length=30)
    code = models.CharField(verbose_name="код провайдера", max_length=10)
    is_active = models.BooleanField(verbose_name="активно?")

    def __str__(self):
        return f'{self.name}'


class Tags(models.Model):
    provider_tag_id = models.IntegerField()
    title = models.CharField(max_length=1024)
    parent = models.TextField(null=True, blank=True)
    children = models.TextField(null=True, blank=True)
    parents = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Courses(models.Model):
    EASY = 'EASY'
    INTERMEDIATE = 'IN'
    ADVANCED = 'AD'

    DIFFICULTIES_CHOICES = [
        (EASY, 'easy'),
        (INTERMEDIATE, 'Intermediate'),
        (ADVANCED, 'Advanced'),
    ]

    title = models.CharField(max_length=256)
    title_en = models.CharField(max_length=256)
    provider_course_id = models.PositiveIntegerField("id курса в провайдера", null=True, blank=True)
    provider = models.ForeignKey(to=Provider, verbose_name="провайдер", on_delete=models.PROTECT, null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    cover = models.TextField("ссылка на изображение курса", null=True, blank=True)
    target_audience = models.TextField("для кого", null=True, blank=True)
    requirements = models.TextField("требования", null=True, blank=True)
    description = models.TextField("описание", null=True, blank=True)
    total_units = models.CharField(max_length=256, null=True, blank=True)
    lessons_count = models.CharField(max_length=256, null=True, blank=True)
    quizzes_count = models.CharField(max_length=256, null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    price = models.CharField(max_length=20, null=True, blank=True)
    currency_code = models.CharField(max_length=10, null=True, blank=True)
    is_archived = models.BooleanField(default=False)
    difficulty = models.CharField(max_length=10, null=True, blank=True)
    acquired_skills = models.TextField("чему вы научитесь", null=True, blank=True)
    acquired_assets = models.TextField("что вы получаете", null=True, blank=True)
    learning_format = models.TextField("как проходит обучение", null=True, blank=True)
    course_type = models.CharField(max_length=10) # TODO: choices?
    with_certificate = models.BooleanField(default=False)
    canonical_url = models.TextField()
    is_active = models.BooleanField(default=True)
    is_sent = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'


class Author(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.title}'


class CourseAuthor(models.Model):
    course = models.ForeignKey(to=Courses, on_delete=models.CASCADE)
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.course._title} {self.author.title}'


class Sections(models.Model):
    provider_lesson_id = models.PositiveIntegerField("id секцию в провайдера")
    course = models.ForeignKey(to=Courses, on_delete=models.CASCADE)
    position = models.PositiveIntegerField()
    description = models.TextField()
    title = models.CharField(max_length=1024)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'


class Lessons(models.Model):
    provider_lesson_id = models.PositiveIntegerField("id урока в провайдера")
    course = models.ForeignKey(to=Courses, on_delete=models.CASCADE)
    title = models.TextField()


class Units(models.Model):
    provider_unit_id = models.PositiveIntegerField()
    lesson = models.ForeignKey(to=Lessons, on_delete=models.CASCADE)
    section = models.ForeignKey(to=Sections, on_delete=models.CASCADE, null=True, blank=True)


class Assignments(models.Model):
    provider_assignment_id = models.PositiveIntegerField()
    unit = models.ForeignKey(to=Units, on_delete=models.CASCADE)
    lesson = models.ForeignKey(to=Lessons, on_delete=models.CASCADE)


class Steps(models.Model):
    provider_step_id = models.PositiveIntegerField()
    position = models.PositiveIntegerField()
    block = models.JSONField()
    is_enabled = models.BooleanField(default=True)

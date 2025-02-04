# Generated by Django 5.0.8 on 2025-02-02 21:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cources', '0007_alter_units_section'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
            ],
        ),
        migrations.AlterField(
            model_name='courses',
            name='lessons_count',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='courses',
            name='provider_course_id',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='id курса в провайдера'),
        ),
        migrations.AlterField(
            model_name='courses',
            name='quizzes_count',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='courses',
            name='total_units',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.CreateModel(
            name='CourseAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cources.author')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cources.courses')),
            ],
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-21 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_escola', '0002_remove_classroom_name_remove_schoolsubjects_teacher_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='school_subjects',
        ),
    ]

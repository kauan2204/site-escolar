# Generated by Django 4.2.3 on 2023-07-23 13:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_escola', '0010_alter_quizquestion_n_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizquestion',
            name='n_options',
            field=models.IntegerField(default=1, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9)]),
        ),
    ]

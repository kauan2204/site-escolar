# Generated by Django 4.2.3 on 2023-07-21 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_escola', '0004_quizoptions_remove_schoolsubjects_classroom_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizoptions',
            name='from_quiz',
        ),
        migrations.CreateModel(
            name='QuizQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('from_quiz', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='site_escola.quiz')),
            ],
        ),
        migrations.AddField(
            model_name='quizoptions',
            name='from_question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='site_escola.quizquestion'),
        ),
    ]

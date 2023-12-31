# Generated by Django 4.2.3 on 2023-07-19 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_escola', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classroom',
            name='name',
        ),
        migrations.RemoveField(
            model_name='schoolsubjects',
            name='teacher',
        ),
        migrations.AddField(
            model_name='classroom',
            name='serie',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='classroom',
            name='turma',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='teacher',
            name='schoolsubjects',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='site_escola.schoolsubjects'),
        ),
    ]

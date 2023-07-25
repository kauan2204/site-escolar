from django.contrib import admin
from site_escola import models

# Register your models here.
@admin.register(models.Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(models.QuizQuestion)
class QuizQuestionAdmin(admin.ModelAdmin):
    ...


@admin.register(models.QuizOptions)
class QuizOptionsAdmin(admin.ModelAdmin):
    ...
from django.db import models
from django.utils import timezone


# Create your models here.

class Quiz(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.name
    
class QuizQuestion(models.Model):
    content = models.TextField()
    n_options = models.IntegerField(blank=True, null=True)
    from_quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.content


class QuizOptions(models.Model):
    content = models.TextField()
    from_question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.content
    

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class QuizResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE);
    timestamp = models.DateTimeField(auto_now_add=True);

    question_1 = models.CharField(max_length=20)
    question_2 = models.CharField(max_length=20)
    question_3 = models.CharField(max_length=20)
    question_4 = models.CharField(max_length=20)
    question_5 = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Quiz Result'
        verbose_name_plural = 'Quiz Results'

    def __str__(self):
        return f'{self.user.username} - {self.timestamp}'

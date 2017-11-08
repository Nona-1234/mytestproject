from django.db import models


# Create your models here.

class Question_Text(models.Model):
    question_no = models.IntegerField()
    question_text = models.CharField(max_length=200)
    answer = models.TextField(max_length=220)

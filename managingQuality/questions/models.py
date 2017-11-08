from django.db import models


# Create your models here.

class Questions(models.Model):
    question_no = models.IntegerField()
    question_text = models.CharField(max_length=200)
    degree = models.CharField(max_length=100)
    question_type = models.CharField(max_length=100)
    question_category = models.CharField(max_length=100)
    specialist_department = models.CharField(max_length=200)

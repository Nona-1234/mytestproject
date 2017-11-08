from django.db import models


# Create your models here.

class Course_Structures(models.Model):
    week_no = models.IntegerField()
    hours = models.IntegerField()
    lecture_name = models.CharField(max_length=150)
    lecture_contents = models.CharField(max_length=200)
    teaching_method = models.CharField(max_length=200)
    assessment_method = models.CharField(max_length=200)



from django.db import models


# Create your models here.

class Department(models.Model):
    department = models.CharField(max_length=64)




    def __str__(self):
       return self.department


class Subjects(models.Model):

    title = models.CharField(max_length=128)
    case = models.CharField(max_length=6)
    course = models.CharField(max_length=7)
    department = models.ForeignKey('Department')
    stage = models.CharField(max_length=6)
    study = models.CharField(max_length=10)


    def __str__(self):
       return self.title





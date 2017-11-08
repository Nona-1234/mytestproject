from django.db import models


# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=32)
    second_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField()
    phone = models.CharField(max_length=11)


    def __str__(self):
        return self.first_name

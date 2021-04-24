from django.db import models

# Create your models here.

class Student(models.Model):
  name = models.CharField(max_length=100)
  registration_number = models.CharField(max_length=10)
  email = models.EmailField()
  date_of_birth = models.DateField()
  hometown = models.CharField(max_length=100)
  score = models.FloatField()
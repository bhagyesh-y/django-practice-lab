from django.db import models
class Student(models.Model):
    rollno= models.IntegerField()
    name = models.CharField(max_length=20)
    marks = models.FloatField()
    add = models.CharField(max_length=50)
# Create your models here.


from django.db import models

# Create your models here.
class Employee(models.Model):
    ename=models.CharField(max_length=20)
    esal=models.FloatField()
    add=models.CharField(max_length=200)
    
class Student(models.Model):
    sname=models.CharField(max_length=20)
    sroll=models.FloatField()
    sadd=models.CharField(max_length=200)
    
class Teacher(models.Model):
    tname=models.CharField(max_length=20)
    troll=models.FloatField()
    tadd=models.CharField(max_length=200)
    
class Book(models.Model):
    bname=models.CharField(max_length=20)
    bauthor=models.CharField(max_length=20)    
    bprice=models.FloatField()
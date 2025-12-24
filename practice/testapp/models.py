from django.db import models

# Create your models here.
job_title=[
    ("Developer","Developer"),
    ("Marketing","Marketing"),
    ("VP","VP"),
    ("CTO","CTO")
]

qual=[
    ("btech","btech"),
    ("mtech","mtech"),
    ("bcs","bcs"),
    ("msc","msc"),
]

mode=[
    ("WFH","WFH"),
    ("Hybrid","Hybrid"),
    ("Office","Office")
]

class Mumbai(models.Model):
    company_name = models.CharField(max_length=25)
    job_title = models.CharField(max_length=15,choices=job_title)
    sal=models.IntegerField()
    qualification=models.CharField(max_length=15,choices=qual)
    joining_date=models.DateField()
    location=models.CharField(max_length=25)
    mode=models.CharField(max_length=25,choices=mode)
    
class Pune(models.Model):
    company_name = models.CharField(max_length=25)
    job_title = models.CharField(max_length=15,choices=job_title)
    sal=models.IntegerField()
    qualification=models.CharField(max_length=15,choices=qual)
    joining_date=models.DateField()
    location=models.CharField(max_length=25)
    mode=models.CharField(max_length=25,choices=mode)
    
class Bengluru(models.Model):
    company_name = models.CharField(max_length=25)
    job_title = models.CharField(max_length=15,choices=job_title)
    sal=models.IntegerField()
    qualification=models.CharField(max_length=15,choices=qual)
    joining_date=models.DateField()
    location=models.CharField(max_length=25)
    mode=models.CharField(max_length=25,choices=mode) 
    
class Hydrabad(models.Model):
    company_name = models.CharField(max_length=25)
    job_title = models.CharField(max_length=15,choices=job_title)
    sal=models.IntegerField()
    qualification=models.CharField(max_length=15,choices=qual)
    joining_date=models.DateField()
    location=models.CharField(max_length=25)
    mode=models.CharField(max_length=25,choices=mode) 
    
class Chennai(models.Model):
    company_name = models.CharField(max_length=25)
    job_title = models.CharField(max_length=15,choices=job_title)
    sal=models.IntegerField()
    qualification=models.CharField(max_length=15,choices=qual)
    joining_date=models.DateField()
    location=models.CharField(max_length=25)
    mode=models.CharField(max_length=25,choices=mode) 
    
class Delhi(models.Model):
    company_name = models.CharField(max_length=25)
    job_title = models.CharField(max_length=15,choices=job_title)
    sal=models.IntegerField()
    qualification=models.CharField(max_length=15,choices=qual)
    joining_date=models.DateField()
    location=models.CharField(max_length=25)
    mode=models.CharField(max_length=25,choices=mode) 
from django.db import models

# Create your models here.

class Product(models.Model):
    pname = models.CharField(max_length=20)
    price=models.FloatField()
    quantity=models.IntegerField()
    # image=models.ImageField(upload_to='imges/')
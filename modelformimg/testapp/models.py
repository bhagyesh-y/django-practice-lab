from django.db import models

class Product(models.Model):
    pname = models.CharField(max_length=20)
    price=models.FloatField()
    quantity=models.IntegerField()
    image=models.ImageField(upload_to='images/')
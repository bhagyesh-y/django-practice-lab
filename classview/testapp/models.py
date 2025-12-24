from django.db import models
from django.urls import reverse
class Beer(models.Model):
    name=models.CharField(max_length=20)
    color=models.CharField(max_length=15)
    price=models.IntegerField()
    
    def get_absolute_url(self):
        return reverse("list")


from django.db import models

class Hero(models.Model):
    name=models.CharField(max_length=20)
    film=models.CharField(max_length=20)
    power=models.CharField(max_length=20)
    
    
    def __str__(self):
        return self.name
    

from django.db import models

class Fruit(models.Model):
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    taste = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

from django.db import models
class Card(models.Model):
    name=models.CharField(max_length=20)
    mail=models.EmailField(max_length=30)
    number = models.IntegerField()
    
    def __str__(self):
        return self.name
    
# Create your models here.

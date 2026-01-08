from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=20)
    last_name= models.CharField(max_length=20)
    photo = models.ImageField(upload_to='photos')
    designation = models.CharField(max_length=50)
    email = models.EmailField(max_length=50 , unique=True)
    phone_number = models.CharField(max_length=12,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__ (self): # string representation of model in db
        return self.first_name
    
 
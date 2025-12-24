from django.db import models
from django.contrib.auth.models import User
# class Page(models.Model):
#     author=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
#     pageName=models.CharField(max_length=50)
    
#     def __str__(self):
#         return f"Author:{self.author} Page:{self.pageName}"
    
class Page2(models.Model):
    author=models.ForeignKey(User,on_delete=models.PROTECT)
    pageName=models.CharField(max_length=50)
    
    def __str__(self):
        return f"Author:{self.author} Page:{self.pageName}"
# Create your models here.

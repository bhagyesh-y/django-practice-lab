from django import forms 
from django.core.validators import *
from django.core.exceptions import ValidationError



class EmployeeForm(forms.Form):
    ename = forms.CharField()
    esal = forms.FloatField()
    add  = forms.CharField()
    
    def clean_ename(self):
       inputEname = self.cleaned_data['ename']   
       if len(inputEname)<6:
           raise ValidationError("Name should be at least 6 characers")
       return inputEname 
   
   
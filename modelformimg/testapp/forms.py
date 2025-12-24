from django import forms
from testapp.models import Product
class Productform(forms.ModelForm):
    class Meta:
        model=Product
        fields= '__all__' 
        widgets = {
            'pname': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
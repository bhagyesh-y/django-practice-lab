from django import forms
from .models import Card

class ContactForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['name', 'mobile', 'mail']
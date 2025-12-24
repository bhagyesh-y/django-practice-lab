from django import forms

class EmployeeForm(forms.Form):
    Name=forms.CharField()
    Email=forms.EmailField()
    Rollno=forms.IntegerField()
    Feedback=forms.CharField(max_length=250,widget=forms.Textarea)
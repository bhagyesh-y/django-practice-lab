from django.shortcuts import render
from formapp . form import EmployeeForm

def empForm_view(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid(): 
            print("Name is :",form.cleaned_data['ename'])
            print("Salary is :",form.cleaned_data['esal'])
            print("Address is :",form.cleaned_data['add'])
    return render(request,'formapp/form.html',{'form':form})    
        



# Create your views here.

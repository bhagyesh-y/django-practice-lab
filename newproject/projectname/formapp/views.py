from django.shortcuts import render
from formapp.forms import EmployeeForm

def empform_view(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            print("Name is:" , form.cleaned_data['Name'])
            print("Email  is:" , form.cleaned_data['Email'])
            print("Roll No is:" , form.cleaned_data['Rollno'])
            print("Feedback is:" , form.cleaned_data['Feedback'])
            
    return render(request,'formapp/form.html',{'form':form})        
            
        

# Create your views here.
#feedback form with name,mail,rollno and feedback
from django.http import HttpResponse
from django.shortcuts import render
from Employees.models import Employee

def home(request):
    employees = Employee.objects.all()
    context={
        'employees':employees,
    }
    print(employees)
    return render (request,"home.html",context)
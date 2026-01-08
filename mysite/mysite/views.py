from django.http import Http404, HttpResponse
from django.shortcuts import render
from Employees.models import Employee

def home(request):
    employees = Employee.objects.all() # all is used to take out all data from db
    context={
        'employees':employees,
    }
    # print(employees)
    return render (request,"home.html",context)


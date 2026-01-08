from django.shortcuts import render,get_object_or_404
from django.http import Http404,HttpResponse
from Employees.models import Employee

def employee_detail(request,pk):
    # try:
    #     employee = Employee.objects.get(pk=pk) # get is used to taking out individual item from db along with primary key 
    #     print("The employee is",employee)
    # except:
    #     raise Http404
            employee = get_object_or_404(Employee,pk=pk)
            print(employee)
            return HttpResponse(employee)
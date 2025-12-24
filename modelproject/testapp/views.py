from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import Employee
from testapp.models import Student
from testapp.models import Teacher
from testapp.models import Book

def emp_list_view(request):
    emplist=Employee.objects.all()
    return render(request,'emplist.html',{'emplist':emplist})

def stud_list_view(request):
    studlist=Student.objects.all()
    return render(request,'studlist.html',{'studlist':studlist})

def teach_list_view(request):
    teachlist=Teacher.objects.all()
    return render(request,'teachlist.html',{'teachlist':teachlist})
 
def book_list_view(request):
    booklist=Book.objects.all()
    return render(request,'booklist.html',{'booklist':booklist}) 

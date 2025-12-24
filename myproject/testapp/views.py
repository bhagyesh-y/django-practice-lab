from django.shortcuts import render
from testapp.models import Student
from django.http import HttpResponse
def student_view(request):
    stu_list=Student.objects.all()
    return render(request,"testapp/Student.html",{'stu_list':stu_list})

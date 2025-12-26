from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student ,Teacher
from .serializers import StudentSerializer
from rest_framework.response import  Response
from rest_framework import status
from rest_framework.decorators import api_view

def teachersview(request):
    teachers= Teacher.objects.all()
    teachers_list=list(teachers.values())
    return JsonResponse(teachers_list,safe=False)
 # by default jsonresponse expects to be dictionary
#  this is manual way to serializing data . converting query set to a list can be a temp solution. While developing RESTful APIs it is not recommended
    
""" that is when drf comes into play . DRF provides us powerful tool called serilizers to convert complex model objects or query sets into json or xml format """


@api_view(['GET'])
def studentsview(request):
    if request.method == 'GET':
        # get all the data from student table 
        students = Student.objects.all()
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
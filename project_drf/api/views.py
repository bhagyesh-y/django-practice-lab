from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from .serializers import StudentSerializer,EmployeeSerializer,FriendSerializer,CricketerSerializer,FruitSerializer,HeroSerializer
from rest_framework.response import  Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employees.models import Employee
from friends.models import Friend
from cricketers.models import Cricketer
from students.models import Student ,Teacher
from fruits.models import Fruit
from heroes.models import Hero
from django.http import Http404
from rest_framework import mixins , generics , viewsets



# manual way of converting query set to a list
def teachersview(request):
    teachers= Teacher.objects.all()
    teachers_list=list(teachers.values())
    return JsonResponse(teachers_list,safe=False)
 # by default jsonresponse expects to be dictionary
#  this is manual way to serializing data . converting query set to a list can be a temp solution. While developing RESTful APIs it is not recommended
    
""" that is when drf comes into play . DRF provides us powerful tool called serilizers to convert complex model objects or query sets into json or xml format """

# below are function based views 
@api_view(['GET','POST'])
def studentsview(request):
    if request.method == 'GET':
        # get all the data from student table 
        students = Student.objects.all()
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST )
    
@api_view(['GET','PUT','DELETE'])      
def studentDetailview(request,pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == "GET":
        serializer = StudentSerializer(student)
        return Response(serializer.data,status=status.HTTP_200_OK) 
    elif request.method == 'PUT':
        serializer = StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)    
        else:    
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST ) 
    elif request.method == 'DELETE':
     student.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)     
 
#   below are class based views 
class Employees(APIView):
    def get(self,request):
        employees = Employee.objects.all()
        serilizer = EmployeeSerializer(employees,many=True)
        return Response(serilizer.data,status=status.HTTP_200_OK)
        
    def post(self,request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST )

class EmployeeDetail(APIView):
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
          raise Http404
      
    def get(self,request,pk):
           employee=self.get_object(pk)
           serializer=EmployeeSerializer(employee)
           return Response(serializer.data,status=status.HTTP_200_OK)
       
    def put(self,request,pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# below used mixins , which reduces the lines of code ridiculously for crud operations

class Friends(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
    
    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)
    
    
class FriendDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,generics.DestroyAPIView,generics.GenericAPIView):
    
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
    
    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)
    
#  Generics for multiple objects 
    
class Cricketers(generics.ListCreateAPIView):
    queryset = Cricketer.objects.all()
    serializer_class = CricketerSerializer
    
    #  Generics for individual object
class CricketerDetail(generics.RetrieveUpdateDestroyAPIView):  
    queryset = Cricketer.objects.all()
    serializer_class = CricketerSerializer
    lookup_field = 'pk'
     
     
     
#Viewets 
class FruitViewset(viewsets.ViewSet):
    def list (self,request):
        queryset = Fruit.objects.all()
        serializer = FruitSerializer(queryset,many = True)
        return Response (serializer.data)
    
    def create(self,request):
        serializer = FruitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
        
    def retrieve(self,request,pk=None):
        fruit = get_object_or_404(Fruit,pk=pk)
        serializer = FruitSerializer(fruit)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def update(self,request,pk=None):
        fruit=get_object_or_404(Fruit,pk=pk)
        serializer=FruitSerializer(fruit,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
        
    def delete(self,request,pk=None):
        fruit=get_object_or_404(Fruit,pk=None)
        fruit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# Viewset.Model which will actually take less lines of code in compared of viewsets
class HeroViewset(viewsets.ModelViewSet):
    queryset=Hero.objects.all()
    serializer_class=HeroSerializer
        
        
    
from rest_framework import serializers
from students.models import Student
from employees.models import Employee
from friends.models import Friend
from cricketers.models import Cricketer
from fruits.models import Fruit
from heroes.models import Hero


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        
        
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"    
            
        
class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = "__all__"        
        
        
class CricketerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cricketer
        fields = "__all__"        
        
        
class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruit
        fields = "__all__"        
        
        
class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = "__all__"        
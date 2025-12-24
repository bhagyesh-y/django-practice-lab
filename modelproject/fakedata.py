import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','modelproject.settings')
django.setup()

import faker 
from random import *
from math import *
f = faker.Faker()
from testapp.models import Student

def generate_data(n):
    for i in range(n):
        fname=f.name()
        froll=f.random_int(min=10,max=100)
        fadd = f.address()

        
        student_list=Student.objects.get_or_create(sroll=froll,sname=fname,sadd=fadd,)
        
generate_data(10)        
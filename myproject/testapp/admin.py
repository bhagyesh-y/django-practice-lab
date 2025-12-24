from django.contrib import admin
from testapp.models import Student
class StudentAdmin(admin.ModelAdmin):
    list_display=['rollno','name','marks','add']
admin.site.register(Student,StudentAdmin)    

# Register your models here.

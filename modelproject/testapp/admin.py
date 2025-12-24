from django.contrib import admin
from testapp.models import Employee
from testapp.models import Student
from testapp.models import Teacher
from testapp.models import Book

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=('id','ename','esal','add')
admin.site.register(Employee,EmployeeAdmin)    

class StudentAdmin(admin.ModelAdmin):
    list_display=('id','sname','sroll','sadd')
admin.site.register(Student,StudentAdmin)    
    
class TeacherAdmin(admin.ModelAdmin):
    list_display=('id','tname','troll','tadd')
admin.site.register(Teacher,TeacherAdmin)    

class BookAdmin(admin.ModelAdmin):
    list_display=('id','bname','bauthor','bprice')
admin.site.register(Book,BookAdmin)    


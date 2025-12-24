from django.contrib import admin
from testapp.models import Mumbai,Pune,Bengluru,Hydrabad,Chennai,Delhi

# Register your models here.
class MumbaiAdmin(admin.ModelAdmin):
    list_display=['company_name','job_title','sal','qualification','joining_date','location','mode'] 
admin.site.register(Mumbai,MumbaiAdmin)  
    
class PuneAdmin(admin.ModelAdmin):
    list_display=['company_name','job_title','sal','qualification','joining_date','location','mode']  
admin.site.register(Pune,PuneAdmin) 

class BengluruAdmin(admin.ModelAdmin):
    list_display=['company_name','job_title','sal','qualification','joining_date','location','mode']  
admin.site.register(Bengluru,BengluruAdmin)   

class HydrabadAdmin(admin.ModelAdmin):
    list_display=['company_name','job_title','sal','qualification','joining_date','location','mode']
admin.site.register(Hydrabad,HydrabadAdmin)    
  
class ChennaiAdmin(admin.ModelAdmin):
    list_display=['company_name','job_title','sal','qualification','joining_date','location','mode']
admin.site.register(Chennai,ChennaiAdmin)    

class DelhiAdmin(admin.ModelAdmin):
    list_display=['company_name','job_title','sal','qualification','joining_date','location','mode'] 
admin.site.register(Delhi,DelhiAdmin)    
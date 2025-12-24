from django.contrib import admin
from testapp.models import Beer
class BeerAdmin(admin.ModelAdmin):
    list_display=['name','color','price']
admin.site.register(Beer,BeerAdmin)
# Register your models here.

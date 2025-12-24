from django.contrib import admin
from testapp.models import Card
class CardAdmin(admin.ModelAdmin):
    list_display=['name','mail','number']
admin.site.register(Card,CardAdmin)    

# Register your models here.

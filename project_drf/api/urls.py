from django.urls import path
from . import views

urlpatterns = [
    path('students/',views.studentsview),
    path('teachers/',views.teachersview)
    
]

from django.urls import path
from .views import create_blog, show_blogs

urlpatterns = [
    path('create/', create_blog, name='create_blog'),
    path('', show_blogs, name='show_blogs'),
]

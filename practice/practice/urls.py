"""
URL configuration for practice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index_view),
    path('mumbai/', views.mumbai_view),
    path('pune/', views.pune_view),
    path('bengluru/',views.bengluru_view),
    path('hyderabad/',views.hydrabad_view),
    path('chennai/',views.chennai_view),
    path('delhi/',views.delhi_view)
]


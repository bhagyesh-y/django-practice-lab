from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home_view(request):
    return render(request,'home.html')

@login_required
def python_view(request):
    return render(request,'demo.html')

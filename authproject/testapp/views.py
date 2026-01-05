from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import SignupForm
from django.http import  HttpResponseRedirect

# Create your views here.
def home_view(request):
    return render(request,'testapp/home.html')

@login_required
def pyt_view(request):
    return render(request,'testapp/python.html')

def js_view(request):
    return render(request,'testapp/js.html')

def logout_view(request):
    logout(request)
    return render(request,'testapp/logout.html')

def signup_view(request):
    form=SignupForm()
    if request.method=="POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
        return HttpResponseRedirect("/accounts/login")
    return render (request,'testapp/signup.html'),{'form':form}   
    
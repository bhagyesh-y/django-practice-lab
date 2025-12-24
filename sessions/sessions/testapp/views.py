from django.shortcuts import render

def name_view(request):
    return render (request , 'testapp/name.html')

def age_view(request):
    name = request.GET['uname']
    request.session['uname']=name
    response = render(request,'testapp/age.html' , {'name':name})
    return response

def qual_view(request):
    age = request.GET['uage']
    request.session['uage']=age
    response = render(request,'testapp/qual.html')
    return response

def res_view(request):
    qual = request.GET['uqual']
    name = request 

# Create your views here.

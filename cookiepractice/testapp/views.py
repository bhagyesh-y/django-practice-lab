from django.shortcuts import render

# Create your views here.
def name_view(request):
    return render(request,'testapp/name.html')

def age_view(request):
    name=request.GET['uname']
    response=render(request,'testapp/age.html',{'name':name})
    response.set_cookie('name',name)
    return response

def qualification_view(request):
    age=request.GET['uage']
    response=render(request,'testapp/qual.html')
    response.set_cookie('age',age)
    return response

def result_view(request):
    qual=request.GET['uqual']
    name=request.COOKIES['name']
    age=request.COOKIES['age']
    return render (request,'testapp/result.html',{'name':name,'age':age,'qual':qual})
from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'home.html')

def about_view(request):
    return render(request,'about.html')

def pagecount(request):
    if 'count' in request.COOKIES:
        newcount=int(request.COOKIES['count'])+1
    else:
        newcount=1
    request.COOKIES['count']=newcount
    response=render(request,'count.html',{'count':newcount})  
    response.set_cookie('count',newcount)
    return response  
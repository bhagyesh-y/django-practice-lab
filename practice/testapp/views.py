from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import Mumbai
from testapp.models import Pune
from testapp.models import Bengluru
from testapp.models import Hydrabad
from testapp.models import Chennai
from testapp.models import Delhi

# Create your views here.
def index_view(request):
    return render(request,'index.html')

def mumbai_view(request):
    mumbai_list=Mumbai.objects.all()
    return render (request,'mumbai.html',{'mumbai_list':mumbai_list})

def pune_view(request):
    pune_list=Pune.objects.all()
    return render (request,'pune.html',{'pune_list':pune_list})

def bengluru_view(request):
    bengluru_list=Bengluru.objects.all()
    return render (request,'bengluru.html',{'bengluru_list':bengluru_list})

def hydrabad_view(request):
    hydrabad_list=Hydrabad.objects.all()
    return render(request,'hydrabad.html',{'hydrabad_list':hydrabad_list})

def chennai_view(request):
    chennai_list=Chennai.objects.all()
    return render (request,'chennai.html',{'chennai_list':chennai_list})

def delhi_view(request):
    delhi_list=Delhi.objects.all()
    return render (request,'delhi.html',{'delhi_list':delhi_list})


    
        
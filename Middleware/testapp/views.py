from django.shortcuts import render
from django.http import HttpResponse

def HelloView(request):
    print("This line is executed by the HelloView")
    # print(10/0)
    return HttpResponse("<h1> This is response fro hello view</h1>")


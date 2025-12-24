from django.shortcuts import render
from django.views import View
from testapp.models import Beer
from django.http import HttpResponse
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy

class HelloView(View):
    def get(self,request):
        return HttpResponse("<h2> Welcome to class based view<h2>")
    
class Tempview(TemplateView):
    template_name="testapp/Hello.html"
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)    
        context["name"] = "bhagyesh"
        context["marks"] =89.19
        context["rollno"]=123
        return context
    
class BeerCreateView(CreateView):
    model = Beer
    fields= "__all__"   
    
class BeerListView(ListView):   
    model = Beer
    
class BeerDetailView(DetailView):
    model =Beer
    
class BeerUpdateView(UpdateView):
    model = Beer
    fields = ['price','color']
    
class BeerDeleteView(DeleteView):
    model = Beer
    success_url=reverse_lazy('list')            
           
    
    
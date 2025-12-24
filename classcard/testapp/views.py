from django.shortcuts import render
from testapp.models import Card
from django.views.generic import CreateView,UpdateView,DeleteView,ListView
from django.urls import reverse_lazy
from django.views import View

class CardListView(ListView):
    def get(self, request):
         cards = Card.objects.all()
         return render(request, 'card_list.html',{'cards':cards})
    
class CardCreateView(CreateView):
    model = Card 
    fields= '__all__'
    success_url=reverse_lazy('home')
    
class CardUpdateView(UpdateView):
    model=Card
    fields=['name','mail','number']
    success_url=reverse_lazy('home')
    
class CardDeleteView(DeleteView):
    model=Card        
    success_url=reverse_lazy('home')
    

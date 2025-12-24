from django.shortcuts import render

# Create your views here.
def count_view(request):
    newcount=request.session.get('count',0)
    newcount=newcount+1
    request.session['count']=newcount
    return render(request,'testapp/count.html',{'count':newcount})

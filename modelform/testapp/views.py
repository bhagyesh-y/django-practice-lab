from django.shortcuts import render,redirect
from  testapp.models import Product
from testapp.forms import ProductForm
from django.contrib import messages


def prolist_view(request):
    pro_list = Product.objects.all()
    return render(request,'testapp/Product.html',{'pro_list':pro_list})


def product_form_view(request):
    form = ProductForm()
    if request.method=="POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Product added successfully!')
        # return prolist_view(request)
        return redirect('product_list')
    return render(request,'testapp/ProductForm.html',{'form':form})     
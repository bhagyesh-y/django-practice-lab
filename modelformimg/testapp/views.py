from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from testapp.forms import Productform
from testapp.models import Product

# ✅ Home Page
@login_required
def home_view(request):
    return render(request, 'home.html')

# ✅ Add Product View
@login_required
def pro_form_view(request):
    if request.method == 'POST':
        form = Productform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = Productform()
    return render(request, 'proform.html', {'form': form})

# ✅ Product List View
@login_required
def pro_view(request):
    pro_list = Product.objects.all()
    return render(request, 'list.html', {'pro_list': pro_list})

# ⚠️ Feedback view — no form to render, just handles POST
# If you're not showing a feedback form separately, you can keep it like this
@login_required
def feedback_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f"Feedback from {name} ({email}): {message}")
        messages.success(request, "Thanks for your feedback!")
    return redirect('home')

# ✅ Optional: Redirect root '/' to login
def redirect_to_login(request):
    return redirect('login')


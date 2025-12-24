from django.shortcuts import render, redirect
from .models import Blog
from django.contrib.auth.models import User
from django import forms
from datetime import date
from django.contrib.auth.decorators import login_required
 
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['heading', 'paragraph', 'image']

@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user  # Assign current user
            blog.save()
            return redirect('show_blogs')
    else:
        form = BlogForm()
    return render(request, 'blog_form.html', {'form': form})

def show_blogs(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'blog_list.html', {
        'blogs': blogs,
        'today': date.today()
    })
 
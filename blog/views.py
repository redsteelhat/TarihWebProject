# views.py

from django.shortcuts import render, get_object_or_404
from .models import Location, BlogPost

def home(request):
    locations = Location.objects.all()
    blog_posts = BlogPost.objects.all()
    return render(request, 'home.html', {'locations': locations, 'blog_posts': blog_posts})

def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'blog_detail.html', {'post': post})

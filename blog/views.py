from datetime import date
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render

from .models import Post



# Create your views here.


def index(request):
    
    posts = Post.objects.all().order_by("-date")
    context = {
        "posts" : posts
    }
    return render(request, "blog/index.html", context)


def posts(request):
    posts = Post.objects.all().order_by("-date")
    context = {
        "posts" : posts
    }
    return render(request, "blog/all_posts.html", context)


def single_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post
    }
    return render(request, "blog/post-detail.html", context)

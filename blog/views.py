
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

from .models import Post



# Create your views here.

class IndexView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
    ordering = "-date"
    paginate_by = 3

class PostsView(ListView):
    model = Post
    template_name = "blog/all_posts.html"
    context_object_name = "posts"
    ordering = "-date"

class SinglePostView(DetailView):
    model = Post
    template_name = "blog/post-detail.html"
    context_object_name = "post"
    slug_field = "slug"

"""
def index(request):
    
    posts = Post.objects.all().order_by("-date")[:3]
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

"""
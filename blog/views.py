
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import CreateView, DetailView, ListView

from .models import Post, Comment
from .forms import CommentForm



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

class SinglePostView(View):
    template_name = "blog/post-detail.html"

    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        comments = Comment.objects.filter(post=post).order_by('-date')
        form = CommentForm()

        context = {
            "post": post,
            "form": form,
            "comments": comments,
        }

        return render(request, self.template_name, context)

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False) 
            comment.post = post
            comment.save()
            return redirect('single-post-page', slug=post.slug)

        comments = Comment.objects.filter(post=post).order_by('-date')
        context = {
            "post": post,
            "form": form,
            "comments": comments,
        }

        return render(request, self.template_name, context)


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
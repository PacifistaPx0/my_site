
from django.shortcuts import render, get_object_or_404
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

class SinglePostView(DetailView):
    model = Post
    template_name = "blog/post-detail.html"
    context_object_name = "post"
    slug_field = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        context["comments"] = Comment.objects.filter(post=self.object)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.save()
            context["form"] = CommentForm()
            context["comments"] = Comment.objects.filter(post=self.object)
            return self.render_to_response(context)
        else:
            context["form"] = form
            context["comments"] = Comment.objects.filter(post=self.object)
            return self.render_to_response(context)


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
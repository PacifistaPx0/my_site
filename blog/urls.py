from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index-page"),
    path("posts", views.posts, name="posts-page"),
    path("posts/<slug>", views.single_post,
         name="single-post-page")  # /posts/my-first-post
]

from django.urls import path
from . import views


urlpatterns = [
    path("", views.IndexView.as_view(), name="index-page"),
    path("posts/", views.PostsView.as_view(), name="posts-page"),
    path("post/<slug:slug>/", views.SinglePostView.as_view(), name="single-post-page"),
]
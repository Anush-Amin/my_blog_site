from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from .models import Post

from django.views.generic import ListView, DetailView

# Create your views here.

# def starting_page(request):
#     latest_posts = Post.objects.all().order_by("-date")[:3]
#     return render(request, "blog/index.html", {
#         "posts": latest_posts
#     })

# Implementing class based view instead of above function based one
## Changes needs to be made in:
## * blog/urls.py
class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"  # name given in blog/templates/blog/index.html

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

# def posts(request):
#     all_posts = Post.objects.all().order_by("-date")
#     return render(request, "blog/all-posts.html", {
#         "all_posts": all_posts
#     })

# Implementing class based view instead of above function based one
## Changes needs to be made in:
## * blog/urls.py
class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"

# def post_detail(request, slug):
#     identified_post = get_object_or_404(Post, slug=slug)
#     return render(request, "blog/post-details.html", {
#         "post": identified_post,
#         "post_tags": identified_post.tags.all()
#     })

# Implementing class based view instead of above function based one
## Changes needs to be made in:
## * blog/urls.py
class SinglePostView(DetailView):
    template_name = "blog/post-details.html"
    model = Post
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tags.all()
        return context

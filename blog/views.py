from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .models import BlogPost, Comment, Like


def index(request):
    posts = BlogPost.objects.filter(published=True)
    return render(request, "blog/list.html", {"posts": posts})


def detail(request, pk: int):
    post = get_object_or_404(BlogPost, pk=pk, published=True)
    return render(request, "blog/detail.html", {"post": post})


@require_POST
def like_post(request, pk: int):
    post = get_object_or_404(BlogPost, pk=pk, published=True)
    Like.objects.create(blog_post=post)
    return redirect("blog:detail", pk=pk)


@require_POST
def comment_post(request, pk: int):
    post = get_object_or_404(BlogPost, pk=pk, published=True)
    name = request.POST.get("name", "Anonymous").strip() or "Anonymous"
    text = request.POST.get("text", "").strip()
    if text:
        Comment.objects.create(blog_post=post, name=name, text=text)
    return redirect("blog:detail", pk=pk)

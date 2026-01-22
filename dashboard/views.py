from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from blog.models import BlogPost
from .forms import BlogPostForm


def staff_required(view):
    return login_required(user_passes_test(lambda u: u.is_staff)(view))


@staff_required
def home(request):
    posts = (
        BlogPost.objects.annotate(
            like_count=Count("likes"), comment_count=Count("comments")
        )
        .all()
        .order_by("-created_at")
    )
    return render(request, "dashboard/home.html", {"posts": posts})


@staff_required
def post_create(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("dashboard:home")
    else:
        form = BlogPostForm()
    return render(request, "dashboard/post_form.html", {"form": form, "mode": "Create"})


@staff_required
def post_edit(request, pk: int):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("dashboard:home")
    else:
        form = BlogPostForm(instance=post)
    return render(request, "dashboard/post_form.html", {"form": form, "mode": "Edit"})


@staff_required
@require_POST
def post_delete(request, pk: int):
    post = get_object_or_404(BlogPost, pk=pk)
    post.delete()
    return redirect("dashboard:home")


@staff_required
@require_POST
def post_toggle_publish(request, pk: int):
    post = get_object_or_404(BlogPost, pk=pk)
    post.published = not post.published
    post.save(update_fields=["published"])
    return redirect("dashboard:home")


@staff_required
def stats_json(request):
    data = list(
        BlogPost.objects.annotate(like_count=Count("likes"), comment_count=Count("comments"))
        .values("id", "title", "published", "like_count", "comment_count")
        .order_by("-created_at")
    )
    return JsonResponse({"posts": data})

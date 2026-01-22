from django.contrib import admin

from .models import BlogPost, Comment, Like


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "published", "created_at")
    list_filter = ("published",)
    search_fields = ("title",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("blog_post", "name", "created_at")
    search_fields = ("name", "text")


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("blog_post", "created_at")

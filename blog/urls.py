from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),
    path("post/<int:pk>/", views.detail, name="detail"),
    path("post/<int:pk>/like/", views.like_post, name="like"),
    path("post/<int:pk>/comment/", views.comment_post, name="comment"),
]

from django.urls import path

from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.home, name="home"),
    path("posts/new/", views.post_create, name="post_create"),
    path("posts/<int:pk>/edit/", views.post_edit, name="post_edit"),
    path("posts/<int:pk>/delete/", views.post_delete, name="post_delete"),
    path("posts/<int:pk>/toggle/", views.post_toggle_publish, name="post_toggle"),
    path("stats.json", views.stats_json, name="stats_json"),
]

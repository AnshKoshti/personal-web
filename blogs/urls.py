from django.urls import path, include
from . import views

app_name = "blogs"

urlpatterns = [
    path("", views.blogs_list, name="list"),
    path("<slug:slug>", views.blog_page, name="blog_page"),
]

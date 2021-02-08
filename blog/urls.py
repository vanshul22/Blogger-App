from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # handling Home Page of Blog Here
    path("", views.bloghome, name="bloghome"),
    # Handling Any Slug Here
    path("<str:slug>", views.blogpost, name="blogpost"),
]

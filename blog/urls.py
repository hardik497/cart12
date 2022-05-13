
from textwrap import indent
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="BlogHome"),
    path("blogpost/<int:id>", views.blogpost,name="blogpost"),
]


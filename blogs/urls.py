from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "blogs"

urlpatterns = [
    path('', views.allblog, name="allblog"),
    path('<str:blogslug>/', views.eachblog, name="eachblog"),
]

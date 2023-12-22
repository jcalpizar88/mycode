#!/usr/bin/python3

# imports from Django
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('welcome/', views.welcome),
]
# clock/ is the path to trigger our function    
urlpatterns += [path('clock/', views.current_datetime),]

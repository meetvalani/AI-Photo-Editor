from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.object_removal,name='object_removal'),
]

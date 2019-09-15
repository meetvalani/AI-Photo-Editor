from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.blur_to_hd,name='blur_to_hd'),
]

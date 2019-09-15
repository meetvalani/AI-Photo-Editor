from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.image_to_map,name='image_to_map'),
]

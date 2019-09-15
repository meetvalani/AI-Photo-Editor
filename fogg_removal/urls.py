from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.fogg_removal,name='fogg_removal'),
]

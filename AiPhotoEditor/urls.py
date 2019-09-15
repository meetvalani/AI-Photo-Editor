"""AiPhotoEditor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path,include

urlpatterns = [
    #path('', include('calc.urls'))
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('index',include('home.urls')),
    path('fogg_removal',include('fogg_removal.urls')),
    path('object_removal',include('object_removal.urls')),
    path('blur_to_hd',include('blur_to_hd.urls')),
    path('face_aging',include('face_aging.urls')),
    path('image_to_map',include('image_to_map.urls')),
]

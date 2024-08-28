"""
URL configuration for Project_Ipl project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from CSK.views import *
from MI.views import *
from RCB.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('msd/',msd,name='msd'),
    path('jaddu/',jaddu,name='jaddu'),
    path('Rohit/',Rohit,name='Rohit'),
    path('Bumrah/',Bumrah,name='Bumrah'),
    path('Virat/',Virat,name='Virat'),
    path('Siraj/',Siraj,name='Bumrah'),
]

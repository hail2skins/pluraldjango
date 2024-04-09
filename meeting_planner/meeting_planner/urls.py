"""
URL configuration for meeting_planner project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include # Import the include function
from website.views import welcome # Import the welcome view
from website.views import about # Import the about view
import django.contrib.auth.urls # Import the authentication views provided by Django

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", welcome, name="home"), # Add a URL pattern for the welcome view
    path("about", about), # Add a URL pattern for the about view
    path('meetings/', include('meetings.urls')), # Add a URL pattern for the meetings app which imports urls.py from the meetings app
    path('auth/', include('django.contrib.auth.urls')) # Add a URL pattern for the authentication views that are provided by Django
]

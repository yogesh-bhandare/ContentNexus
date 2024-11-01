"""
URL configuration for home project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from .views import test_view
from landing import views as landing_view

urlpatterns = [
    path('', landing_view.home_page_view, name="home"),
    path('home/', landing_view.home_page_view, name="home"),
    path('items/', include('items.urls')),
    path('projects/', include('projects.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
]

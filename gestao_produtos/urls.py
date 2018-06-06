"""gestao_produtos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from cadastro import urls as pages_urls
from home_login import urls as home_urls
from home_login.views import my_logout
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', include(home_urls)),
    path('login/', auth_views.login, name='login'),
    path('ssslogout/', my_logout, name='logout'),
    path('admin/', admin.site.urls),
    path('produtos/', include(pages_urls)),
]

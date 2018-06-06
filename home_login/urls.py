from django.urls import path, include

from .views import logout, home



urlpatterns = [
    path('', home, name='home'),
    path('logout/', logout, name='logout'),

]
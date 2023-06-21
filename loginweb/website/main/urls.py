from django.urls import path 
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
]
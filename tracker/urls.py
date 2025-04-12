from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('about', views.about, name = "about"),
    path('login', views.login_view, name = "login"),
    path('profile', views.profile, name = "profile"),
    path('register', views.register, name = "register"),
    path('logout/', views.logout_view, name='logout'),
]

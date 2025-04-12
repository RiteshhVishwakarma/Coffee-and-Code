from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name = "home"),
    path('about', views.about, name = "about"),
    path('login', views.login_view, name = "login"),
    path('profile', views.profile, name = "profile"),
    path('register', views.register, name = "register"),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

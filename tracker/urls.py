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
    path('logpage/', views.log, name='logpage'),

    # Dividing Log
    path('log/water/', views.add_water, name='log_water'),
    path('log/calories/', views.add_calories, name='log_calories'),
    path('log/exercise/', views.add_exercise, name='log_exercise'),
    path('weekly-log/', views.weekly_log, name='weekly_log'),
]

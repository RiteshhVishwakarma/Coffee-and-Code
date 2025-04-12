from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .forms import CustomUserRegistrationForm, CustomLoginForm
from django.contrib.auth.decorators import login_required

# Dashboard Page View
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def profile(request):
    return render(request, 'profile.html')

def home(request): 
    return render(request, 'home.html')

# Login View
# tracker/views.py
def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth_login(request, user)
                return redirect('dashboard')  # Redirect to dashboard or any other page
            else:
                messages.error(request, 'Invalid credentials')
    else:
        form = CustomLoginForm()
    
    return render(request, 'login.html', {'form': form})

# Registration View
def register(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = CustomUserRegistrationForm()
    
    return render(request, 'register.html', {'form': form})

# Logout View
def logout_view(request):
    auth_logout(request)
    return redirect('home')  # Redirect to home page after logging out

# About Page View
def about(request):
    return render(request, 'about.html')

# Profile Page View
def profile(request):
    return render(request, 'profile.html')

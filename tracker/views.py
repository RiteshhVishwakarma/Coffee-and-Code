from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .forms import CustomUserRegistrationForm, CustomLoginForm
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from .models import DailyLog
# from datetime import date

# Dashboard Page View
@login_required
def dashboard(request):
    today = now().date()
    # Sample values (you can later fetch this from models or form inputs)
    water_intake = 1.5  # in Liters
    water_goal = 2
    calories_consumed = 1800
    calories_goal = 2200
    exercise_done = 45  # in minutes
    exercise_goal = 60

    context = {
        'water_intake': water_intake,
        'water_goal': water_goal,
        'water_percent': round((water_intake / water_goal) * 100),

        'calories_consumed': calories_consumed,
        'calories_goal': calories_goal,
        'calories_percent': round((calories_consumed / calories_goal) * 100),

        'exercise_done': exercise_done,
        'exercise_goal': exercise_goal,
        'exercise_percent': round((exercise_done / exercise_goal) * 100),

        'today': today
    }

    return render(request, 'dashboard.html', context)

@login_required
def log(request):
    if request.method == 'POST':
        calories = request.POST.get('calories_consumed')
        exercise = request.POST.get('exercise_done')
        water = request.POST.get('water_intake')  # Optional if you add it to the model later

        # Save log
        DailyLog.objects.create(
            user=request.user,
            calories_consumed=calories,
            calories_burned=None,  # Add if tracking separately
            excersise_done=exercise
        )
        return redirect('dashboard')  # Or wherever you want to redirect after saving

    return render(request, 'logpage.html')


def current_date(request):
    return {'now': now()}

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

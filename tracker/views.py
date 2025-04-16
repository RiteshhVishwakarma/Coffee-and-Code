from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from datetime import date, timedelta
from .models import Goal
from .forms import GoalForm

from .forms import (
    CustomUserRegistrationForm,
    CustomLoginForm,
    WaterIntakeForm,
    CalorieForm,
    ExerciseForm,
)

from .models import (
    DailyLog,
    Goal,
    WeeklyGoal,
    UserProfile,
)

# Home Page
def home(request): 
    return render(request, 'index.html')

# About Page
def about(request):
    return render(request, 'about.html')

# Login View
def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid credentials')
    else:
        form = CustomLoginForm()
    
    return render(request, 'login.html', {'form': form})

# Register View
def register(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserRegistrationForm()
    
    return render(request, 'register.html', {'form': form})

# Logout View
def logout_view(request):
    auth_logout(request)
    return redirect('home')

# Profile View
@login_required
def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'profile.html', {'profile': user_profile})

# Dashboard View
@login_required
def dashboard(request):
    today = date.today()
    week_ago = today - timedelta(days=7)

    logs = DailyLog.objects.filter(user=request.user, date__gte=week_ago)

    total_water = sum(log.water_intake or 0 for log in logs)
    total_calories = sum(log.calories or 0 for log in logs)
    total_exercise = sum(log.exercise_duration or 0 for log in logs)

    goal, _ = Goal.objects.get_or_create(user=request.user)

    today_log = DailyLog.objects.filter(user=request.user, date=today).first()
    today_water_intake = today_log.water_intake if today_log and today_log.water_intake else 0
    daily_water_goal = 2.0  # litres/day
    water_percent = (today_water_intake / daily_water_goal) * 100 if daily_water_goal > 0 else 0

    context = {
        'water_intake': total_water,
        'water_goal': goal.water_goal,
        'water_percent': int((total_water / goal.water_goal) * 100),

        'total_calories': total_calories,
        'calories_goal': goal.calories_goal,
        'calories_percent': int((total_calories / goal.calories_goal) * 100),

        'total_exercise': total_exercise,
        'exercise_goal': goal.exercise_goal,
        'exercise_percent': int((total_exercise / goal.exercise_goal) * 100),

        'logs': logs,
        'today_water_intake': today_water_intake,
        'today_water_percent': int(water_percent),
    }

    return render(request, 'dashboard.html', context)

# Weekly Summary View
@login_required
def weekly_log(request):
    today = timezone.now().date()
    week_ago = today - timedelta(days=7)

    logs = DailyLog.objects.filter(user=request.user, date__gte=week_ago)

    total_water = sum(log.water_intake or 0 for log in logs)
    total_calories = sum(log.calories or 0 for log in logs)
    total_exercise = sum(log.exercise_duration or 0 for log in logs)

    goal, _ = WeeklyGoal.objects.get_or_create(
        user=request.user,
        defaults={
            'water_goal': 14.0,
            'calorie_goal': 14000,
            'exercise_goal': 210
        }
    )

    water_percentage = (total_water / goal.water_goal) * 100 if goal.water_goal > 0 else 0
    calories_percentage = (total_calories / goal.calorie_goal) * 100 if goal.calorie_goal > 0 else 0
    exercise_percentage = (total_exercise / goal.exercise_goal) * 100 if goal.exercise_goal > 0 else 0

    context = {
        'logs': logs,
        'total_water': total_water,
        'total_calories': total_calories,
        'total_exercise': total_exercise,
        'goal': goal,
        'water_percentage': water_percentage,
        'calories_percentage': calories_percentage,
        'exercise_percentage': exercise_percentage,
    }

    return render(request, 'weekly_log.html', context)

# Log Page (Manual Log Entry)
@login_required
def log(request):
    if request.method == 'POST':
        DailyLog.objects.create(
            user=request.user,
            water=request.POST.get('water_intake'),
            calories=request.POST.get('calories'),
            exercise_duration=request.POST.get('excersise_duration')
        )
        return redirect('dashboard')

    return render(request, 'logpage.html')

# Add Water Intake
@login_required
def add_water(request):
    if request.method == 'POST':
        form = WaterIntakeForm(request.POST)
        if form.is_valid():
            log, _ = DailyLog.objects.get_or_create(user=request.user, date=date.today())
            current_intake = log.water_intake or 0  # Handle None safely
            log.water_intake = current_intake + form.cleaned_data['water_intake']
            log.save()
            return redirect('dashboard')
    else:
        form = WaterIntakeForm()

    return render(request, 'log_water.html', {'form': form})
# Add Calories
@login_required
def add_calories(request):
    if request.method == 'POST':
        form = CalorieForm(request.POST)
        if form.is_valid():
            log, _ = DailyLog.objects.get_or_create(user=request.user, date=date.today())
            current_calories = log.calories or 0  # Handle None safely
            log.calories = current_calories + form.cleaned_data['calories']
            log.save()
            return redirect('dashboard')
    else:
        form = CalorieForm()

    return render(request, 'log_calories.html', {'form': form})

# Add Exercise
@login_required
def add_exercise(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            log, _ = DailyLog.objects.get_or_create(user=request.user, date=date.today())
            current_duration = log.exercise_duration or 0  # Prevent NoneType error
            log.exercise_duration = current_duration + form.cleaned_data['exercise_duration']
            log.save()
            return redirect('dashboard')
    else:
        form = ExerciseForm()

    return render(request, 'log_exercise.html', {'form': form})



@login_required
def edit_goal(request):
    goal, _ = Goal.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = GoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = GoalForm(instance=goal)

    return render(request, 'edit_goal.html', {'form': form})

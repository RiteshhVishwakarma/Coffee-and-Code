from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .forms import CustomUserRegistrationForm, CustomLoginForm
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from .models import DailyLog
# from datetime import date
from .models import WeeklyGoal
from datetime import date, timedelta



# # Dashboard Page View
@login_required
def dashboard(request):
    today = date.today()
    week_ago = today - timedelta(days=7)
    logs = DailyLog.objects.filter(user=request.user, date__gte=week_ago)

    total_water = sum(log.water_intake or 0 for log in logs)
    total_calories = sum(log.calories or 0 for log in logs)
    total_exercise = sum(log.exercise_duration or 0 for log in logs)
    goal, _ = WeeklyGoal.objects.get_or_create(user=request.user)


    context = {
        'logs': logs,
        'total_water': total_water,
        'total_calories': total_calories,
        'total_exercise': total_exercise,
        'goal': goal,
    }
    return render(request, 'dashboard.html', context)



@login_required
def log(request):
    if request.method == 'POST':
        water = request.POST.get('water_intake')
        calories = request.POST.get('calories')
        exercise = request.POST.get('excersise_duration')

        # Save log
        DailyLog.objects.create(
            user=request.user,
            water = request.POST.get('water_intake'),
            calories = request.POST.get('calories'),
            exercise_duration = exercise
        )
        return redirect('dashboard')  # Or wherever you want to redirect after saving

    return render(request, 'logpage.html')


# def current_date(request):
#     return {'now': now()}

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

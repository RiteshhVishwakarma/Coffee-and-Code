from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .forms import CustomUserRegistrationForm, CustomLoginForm
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from .models import DailyLog
# from datetime import date
from .models import WeeklyGoal
# from datetime import date, timedelta, timezone
from datetime import date, timedelta
from django.utils import timezone
from .forms import WaterIntakeForm, CalorieForm, ExerciseForm
from .models import UserProfile


def weekly_log(request):
    today = timezone.now().date()
    week_ago = today - timedelta(days=7)
    
    # Fetch logs for the last week
    logs = DailyLog.objects.filter(user=request.user, date__gte=week_ago)

    # Sum the total water, calories, and exercise
    total_water = sum(log.water_intake or 0 for log in logs)
    total_calories = sum(log.calories or 0 for log in logs)
    total_exercise = sum(log.exercise_duration or 0 for log in logs)

    # Weekly goals
    goal, _ = WeeklyGoal.objects.get_or_create(
        user=request.user,
        defaults={
            'water_goal': 14.0,       # Default 14 liters/week
            'calorie_goal': 14000,    # Default 2000/day × 7
            'exercise_goal': 210      # Default 30 min/day × 7
        }
    )

    # Calculate percentages
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






# ___________________________ working below code
@login_required
def add_water(request):
    if request.method == 'POST':
        form = WaterIntakeForm(request.POST)
        if form.is_valid():
            # Get or create the DailyLog entry for today
            log, created = DailyLog.objects.get_or_create(user=request.user, date=date.today())
            
            # Add the new water intake to the existing intake (if any)
            log.water_intake += form.cleaned_data['water_intake']
            log.save()  # Save the updated value
            
            # Redirect to the dashboard after saving
            return redirect('dashboard')
    else:
        form = WaterIntakeForm()
    
    return render(request, 'log_water.html', {'form': form})


@login_required
def add_calories(request):
    if request.method == 'POST':
        form = CalorieForm(request.POST)
        if form.is_valid():
            # Get or create the DailyLog entry for today
            log, created = DailyLog.objects.get_or_create(user=request.user, date=date.today())
            
            # Add the new calories to the existing calories intake
            log.calories += form.cleaned_data['calories']
            log.save()  # Save the updated value
            
            # Redirect to the dashboard after saving
            return redirect('dashboard')
    else:
        form = CalorieForm()
    
    return render(request, 'log_calories.html', {'form': form})


@login_required
def add_exercise(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            # Get or create the DailyLog entry for today
            log, created = DailyLog.objects.get_or_create(user=request.user, date=date.today())
            
            # Add the new exercise duration to the existing duration
            log.exercise_duration += form.cleaned_data['exercise_duration']
            log.save()  # Save the updated value
            
            # Redirect to the dashboard after saving
            return redirect('dashboard')
    else:
        form = ExerciseForm()
    
    return render(request, 'log_exercise.html', {'form': form})



@login_required
def dashboard(request):
    today = date.today()
    week_ago = today - timedelta(days=7)

    # 7 days ka log
    logs = DailyLog.objects.filter(user=request.user, date__gte=week_ago)

    # Total values from weekly logs
    total_water = sum(log.water_intake or 0 for log in logs)
    total_calories = sum(log.calories or 0 for log in logs)
    total_exercise = sum(log.exercise_duration or 0 for log in logs)

    # Daily goal (you can also use WeeklyGoal and divide by 7 if needed)
    daily_water_goal = 2.0  # in litres
    water_today = DailyLog.objects.filter(user=request.user, date=today).first()
    today_water_intake = water_today.water_intake if water_today and water_today.water_intake else 0

    # Water percentage for today's intake
    water_percent = (today_water_intake / daily_water_goal) * 100 if daily_water_goal > 0 else 0

    context = {
    'water_intake': total_water,
    'water_goal': 2,  # or user's custom goal
    'water_percent': int((total_water / 2) * 100),

    'total_calories': total_calories,
    'calories_goal': 2000,
    'calories_percent': int((total_calories / 2000) * 100),

    'total_exercise': total_exercise,
    'exercise_goal': 60,
    'exercise_percent': int((total_exercise / 60) * 100),

    'logs': logs,
}

    return render(request, 'dashboard.html', context)







# __________________________________________ WORKING below code

# # Dashboard Page View
@login_required
# def dashboard(request):
#     today = date.today()
#     week_ago = today - timedelta(days=7)
#     logs = DailyLog.objects.filter(user=request.user, date__gte=week_ago)

#     total_water = sum(log.water_intake or 0 for log in logs)
#     total_calories = sum(log.calories or 0 for log in logs)
#     total_exercise = sum(log.exercise_duration or 0 for log in logs)
#     # goal, _ = WeeklyGoal.objects.get_or_create(user=request.user)


#     context = {
#         'logs': logs,
#         'total_water': total_water,
#         'total_calories': total_calories,
#         'total_exercise': total_exercise,
#         # 'goal': goal,
#     }
#     return render(request, 'dashboard.html', context)



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
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'profile.html', {'profile': user_profile})

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

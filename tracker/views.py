from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from .forms import CustomUserRegistrationForm
from .models import UserProfile
from django.contrib.auth.decorators import login_required

# ritesh@123 admin pass admin username
# Create your views here.
def home(request):
    # return HttpResponse("HEllo world")
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # ya jo bhi page dikhana ho
    else:
        form = CustomUserRegistrationForm()
    return render(request, 'register.html', {'form': form})















# def register(request):
#     if request.method == 'POST':
#         form = CustomUserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             # Get extra fields from form.cleaned_data
#             name = form.cleaned_data['name']
#             age = form.cleaned_data['age']
#             height = form.cleaned_data['height']
#             weight = form.cleaned_data['weight']
#             gender = form.cleaned_data['gender']

#             # Create UserProfile linked to user
#             UserProfile.objects.create(
#                 user=user,
#                 name=name,
#                 age=age,
#                 height=height,
#                 weight=weight,
#                 gender=gender
#             )
#             return redirect('login')  # Change to your desired redirect
#     else:
#         form = CustomUserRegistrationForm()
#     return render(request, 'signup.html', {'form': form})

def logout(request):
    return render(request, 'logout.html')


def about(request):
    return render(request, 'about.html')

def profile(request):
    return render(request, 'profile.html')
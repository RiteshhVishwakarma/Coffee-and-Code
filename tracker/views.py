from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    # return HttpResponse("HEllo world")
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')


def about(request):
    return render(request, 'about.html')

def profile(request):
    return render(request, 'profile.html')
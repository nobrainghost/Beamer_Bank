from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

def index(request):
    return render(request, 'signup.html')

def signin(request):
    return render(request, 'signin.html')

def signup(request):
    return render(request, 'signup.html')

def home(request):
    return render(request, 'home.html')
def dashboard(request):
    return render(request, 'dashboard.html')

# Create your views here.

from django.shortcuts import render, HttpResponse
from .models import User

def home(request):
    return render(request, 'home.html')

def join(request):
    return render(request, 'join.html')
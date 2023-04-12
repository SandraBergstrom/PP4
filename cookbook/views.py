from django.shortcuts import render, HttpResponse, redirect
from .models import User
from .forms import UserForm
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def join(request):
    if request.method == 'POST':
        form = UserForm(request.POST or None)
        if form.is_valid():
            form.save()
        else: 
            message.danger(request, ('There was an error filling out the form. Please try again!'))
        messages.success(request, ('You are now a member!'))
        return redirect('home')

    else: 
        return render(request, 'join.html')
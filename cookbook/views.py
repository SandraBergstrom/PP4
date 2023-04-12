from django.shortcuts import render, HttpResponse, redirect
from .models import Member
from .forms import MemberForm
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def join(request):
    if request.method == 'POST':
        form = MemberForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, ('You are now a member!'))
        return redirect('home')

    else: 
        return render(request, 'join.html')
from django.shortcuts import render, HttpResponse, redirect
from django.views import generic
from .models import Member, Recipe 
from .forms import MemberForm
from django.contrib import messages

# def home(request):
#     return render(request, 'home.html')

def join(request):
    if request.method == 'POST':
        form = MemberForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, ('You are now a member!'))
        return redirect('home')

    else: 
        return render(request, 'join.html')

class recipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6
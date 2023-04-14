from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
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
        messages.success(request, ('You are now a member. Please log in!'))
        return redirect('login')

    else: 
        return render(request, 'join.html')

class recipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class RecipePost(View):

    def get(self, request, slug, *args, **kwargs):
        query = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(query, slug=slug) # Fix here
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_post.html",
            {
                'recipe': recipe,
                'comments': comments,
                'liked': liked
            },
        )
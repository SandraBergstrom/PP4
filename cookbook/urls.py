from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.recipeList.as_view(), name="home"),
    path('join', views.join, name='join'),
    path('<slug:slug>/', views.RecipePost.as_view(), name='recipe_post'),
]
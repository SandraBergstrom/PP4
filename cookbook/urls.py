from django.urls import path
from . import views


urlpatterns = [
    path("", views.recipeList.as_view(), name="home"),
    path('join', views.join, name='join'),
]
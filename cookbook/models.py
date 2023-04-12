from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class User(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    password = models.CharField(max_length=50)
    food_relation_choices = [
        ('CHEF', 'Chef'),
        ('NUTRITIONIST', 'Nutritionist'),
        ('PASTRY_CHEF', 'Pastry Chef'),
        ('FOOD_STYLIST', 'Food Stylist'),
        ('CULINARY_INSTRUCTOR', 'Culinary Instructor'),
        ('FOOD_CRITIC', 'Food Critic'),
        ('HOME_COOK', 'Home Cook'),
        ('OTHER', 'Other'),
    ]
    food_relation = models.CharField(max_length=30, choices=food_relation_choices, default='HOME_COOK')
    date_joined = models.DateField(auto_now_add=True)


from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Member(models.Model):
    # model for member data
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
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fname} {self.lname}, {self.get_food_relation_display()}"


STATUS = ((0, "Private"), (1, "Public"))

class Ingredient(models.Model):
    quantity = models.FloatField(max_length=2)
    unit = models.CharField(max_length=10)
    name = models.CharField(max_length=200)

class Instruction(models.Model):
    step_number = models.AutoField(primary_key=True)
    description = models.TextField(max_length=1000)

class Recipe(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='recipe_post')
    category_choices = [
        ('APPETIZERS', 'Apperizers'),
        ('BREAKFAST', 'Breakfast'),
        ('MAIN_DISHES', 'Main Dishes'),
        ('DESSERTS', 'Desserts'),
        ('SALLADS', 'Sallads'),
        ('SIDE_DISHES', 'Side Dishes'),
        ('SNACKS', 'Snacks'),
        ('OTHER', 'Other'),
    ]
    category = models.CharField(max_length=30, choices=category_choices)
    prep_time = models.DurationField(blank=True, null=True)
    cooking_time = models.DurationField(blank=True, null=True)
    servings = models.IntegerField()
    description = models.TextField(max_length=1000)
    ingredients = models.ManyToManyField(Ingredient)
    instructions = models.ManyToManyField(Instruction)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on =models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(Member, related_name='recipe_likes')

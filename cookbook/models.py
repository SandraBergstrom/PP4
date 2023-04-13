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


class Ingredient(models.Model):
    # model for ingredients with seperate fields for quantity, unit and ingredient name

    quantity = models.FloatField(max_length=2)
    unit = models.CharField(max_length=10)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.quantity} {self.unit} {self.name}"  


class Instruction(models.Model):
    # model for instructions added by user. Instructions will be automatically numbered starting from 1.

    step_number = models.AutoField(primary_key=True)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return f"{self.step_number}. {self.description}"


STATUS = ((0, "Private"), (1, "Public"))


class Recipe(models.Model):
    # model for recipe

    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='recipe_post')
    category_choices = [
        ('APPETIZERS', 'Appetizers'),
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
    servings = models.IntegerField(default=1)
    excerp = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=1000)
    ingredients = models.ManyToManyField(Ingredient)
    instructions = models.ManyToManyField(Instruction)
    created_on = models.DateField(auto_now_add=True)
    updated_on =models.DateField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='recipe_likes', blank=True)

    class Meta: 
        ordering: ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

class Comment(models.Model):
    # model for comments added to recipes

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering: ['created_on']

    def __str__(self):
        return f"{self.comment} by {self.name}, {self.created_on}"

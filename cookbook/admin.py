from django.contrib import admin
from .models import Member, Recipe, Ingredient, Instruction

admin.site.register(Member)
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Instruction)
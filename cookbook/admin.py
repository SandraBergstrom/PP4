from django.contrib import admin
from .models import Member, Recipe, Ingredient, Instruction
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ['title']}
    summernote_fields = ("description",)

admin.site.register(Member)
# admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Instruction)
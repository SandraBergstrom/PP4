from django.contrib import admin
from .models import Member, Recipe, Ingredient, Instruction, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'created_on', 'category')
    list_filter = ('status', 'created_on', 'category')
    search_fields = ('title', 'author', 'ingredient', 'category')
    prepopulated_fields = {'slug': ['title']}
    summernote_fields = ("description",)

admin.site.register(Member)
admin.site.register(Ingredient)
admin.site.register(Instruction)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'comment', 'recipe', 'created_on', 'approved')
    list_filter = (['created_on', 'approved'])
    search_fields = ('name', 'email', 'comment')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
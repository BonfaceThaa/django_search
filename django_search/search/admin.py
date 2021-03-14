from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}

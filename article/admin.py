from django.contrib import admin
from .models import Article, Comment

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    list_display_links = ['title', 'author']
    list_filter = ['created_date']
    search_fields = ['title']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment_author']
    list_display_links = ['comment_author']
    list_filter = ['comment_date']
    search_fields = ['comment_author']

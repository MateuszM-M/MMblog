from django.contrib import admin
from .models import *



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'published_date', 'created_date', 'updated_date')
    prepopulated_fields = {'slug': ('title',)}
    

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'comment_content', 'created_date', 'active')
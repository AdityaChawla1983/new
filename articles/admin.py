from django.contrib import admin
from django.db import models
from django.db.models.base import Model
from .models import Article, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
class ArticleAdmin(admin.ModelAdmin):
    inlines =[
        CommentInline,
    ]
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)

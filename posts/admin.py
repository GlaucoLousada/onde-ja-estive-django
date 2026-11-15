from django.contrib import admin

from .models import Category, Comment, Post


class CategoryAdmin(admin.ModelAdmin):
    filter_horizontal = ['posts']  # facilita a seleção dos posts da categoria


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category, CategoryAdmin)

from django.contrib import admin

from .models import BlogType,Blog


@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')
    list_per_page = 50
    ordering = ('-id',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'profile', 'author', 'created_time', 'blog_type')
    list_per_page = 50
    ordering = ('-id',)

from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "is_published", "created_at", "updated_at")
    list_filter = ("is_published", "created_at")
    search_fields = ("title", "body")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "name", "email", "is_active", "created_at")
    list_filter = ("is_active", "created_at")
    search_fields = ("name", "email", "body")

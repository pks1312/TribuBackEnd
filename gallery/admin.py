from django.contrib import admin
from .models import GalleryImage


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_active', 'created_at')
    list_filter = ('is_active', 'category', 'created_at')
    search_fields = ('title', 'description', 'category')
    ordering = ('-created_at',)

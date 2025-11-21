from django.contrib import admin
from .models import Professional


@admin.register(Professional)
class ProfessionalAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'bio', 'specialties')
    ordering = ('name',)

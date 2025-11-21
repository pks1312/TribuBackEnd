from django.contrib import admin
from .models import Schedule


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('professional', 'date', 'time', 'is_available', 'created_at')
    list_filter = ('is_available', 'date', 'professional')
    search_fields = ('professional__name',)
    ordering = ('-date', 'time')
    date_hierarchy = 'date'

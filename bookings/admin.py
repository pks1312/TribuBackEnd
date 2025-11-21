from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'service', 'professional', 'date', 'time', 'status', 'created_at')
    list_filter = ('status', 'date', 'professional', 'service')
    search_fields = ('client_name', 'client_email', 'client_phone')
    ordering = ('-date', '-time')
    date_hierarchy = 'date'
    readonly_fields = ('created_at', 'updated_at')

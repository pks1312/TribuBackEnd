from django.contrib import admin
from .models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('author', 'rating', 'service', 'is_approved', 'created_at')
    list_filter = ('is_approved', 'rating', 'created_at')
    search_fields = ('author', 'content')
    ordering = ('-created_at',)
    actions = ['approve_testimonials']

    def approve_testimonials(self, request, queryset):
        queryset.update(is_approved=True)
    approve_testimonials.short_description = "Aprobar testimonios seleccionados"

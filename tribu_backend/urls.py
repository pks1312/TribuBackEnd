from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .health_check import health_check, debug_info, run_migrations

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Health Check y Management
    path('health/', health_check, name='health_check'),
    path('debug/', debug_info, name='debug_info'),
    path('run-migrations/', run_migrations, name='run_migrations'),
    
    # API Endpoints
    path('api/accounts/', include('accounts.urls')),
    path('api/services/', include('services.urls')),
    path('api/professionals/', include('professionals.urls')),
    path('api/schedules/', include('schedules.urls')),
    path('api/bookings/', include('bookings.urls')),
    path('api/testimonials/', include('testimonials.urls')),
    path('api/gallery/', include('gallery.urls')),
]

# Servir archivos media en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
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

from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny
from .models import GalleryImage
from .serializers import GalleryImageSerializer


class GalleryImageViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar imágenes de galería
    """
    queryset = GalleryImage.objects.filter(is_active=True)
    serializer_class = GalleryImageSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at']
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = GalleryImage.objects.filter(is_active=True)
        category = self.request.query_params.get('category', None)
        
        if category:
            queryset = queryset.filter(category=category)
        
        return queryset

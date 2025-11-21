from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny
from .models import Service
from .serializers import ServiceSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar servicios
    """
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'price', 'duration']
    ordering = ['name']

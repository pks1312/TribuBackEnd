from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Testimonial
from .serializers import TestimonialSerializer


class TestimonialViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar testimonios
    """
    serializer_class = TestimonialSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at', 'rating']
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = Testimonial.objects.all()
        
        # Los usuarios públicos solo ven testimonios aprobados
        if not self.request.user.is_staff:
            queryset = queryset.filter(is_approved=True)
        
        service_id = self.request.query_params.get('service_id', None)
        if service_id:
            queryset = queryset.filter(service_id=service_id)
        
        return queryset

    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        """Aprobar un testimonio"""
        testimonial = self.get_object()
        testimonial.is_approved = True
        testimonial.save()
        return Response({'status': 'Testimonio aprobado exitosamente'})

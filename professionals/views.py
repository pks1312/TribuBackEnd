from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.utils import timezone
from datetime import timedelta
from .models import Professional
from .serializers import ProfessionalSerializer


class ProfessionalViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar profesionales
    """
    queryset = Professional.objects.filter(is_active=True)
    serializer_class = ProfessionalSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'bio', 'specialties']
    ordering_fields = ['name']
    ordering = ['name']

    @action(detail=True, methods=['get'])
    def available_dates(self, request, pk=None):
        """Obtener fechas disponibles para un profesional"""
        professional = self.get_object()
        days_ahead = int(request.query_params.get('days', 30))
        
        today = timezone.now().date()
        end_date = today + timedelta(days=days_ahead)
        
        # Importar aquí para evitar dependencia circular
        from schedules.models import Schedule
        
        available_schedules = Schedule.objects.filter(
            professional=professional,
            date__gte=today,
            date__lte=end_date,
            is_available=True
        ).values('date').distinct().order_by('date')
        
        dates = [schedule['date'].isoformat() for schedule in available_schedules]
        return Response({'dates': dates})

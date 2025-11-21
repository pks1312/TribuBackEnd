from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Schedule
from .serializers import ScheduleSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar horarios
    """
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['date', 'time']
    ordering = ['date', 'time']

    def get_queryset(self):
        queryset = Schedule.objects.all()
        professional_id = self.request.query_params.get('professional_id', None)
        date = self.request.query_params.get('date', None)
        is_available = self.request.query_params.get('is_available', None)
        
        if professional_id:
            queryset = queryset.filter(professional_id=professional_id)
        if date:
            queryset = queryset.filter(date=date)
        if is_available is not None:
            queryset = queryset.filter(is_available=is_available.lower() == 'true')
        
        return queryset.order_by('date', 'time')

    @action(detail=False, methods=['post'])
    def bulk_create(self, request):
        """Crear múltiples horarios a la vez"""
        schedules_data = request.data.get('schedules', [])
        created_schedules = []
        
        for schedule_data in schedules_data:
            serializer = self.get_serializer(data=schedule_data)
            if serializer.is_valid():
                serializer.save()
                created_schedules.append(serializer.data)
        
        return Response({
            'created': len(created_schedules),
            'schedules': created_schedules
        }, status=status.HTTP_201_CREATED)

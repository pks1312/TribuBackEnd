from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Booking
from .serializers import BookingSerializer
from schedules.models import Schedule


class BookingViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar reservas
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['date', 'time', 'created_at']
    ordering = ['-date', '-time']

    def get_queryset(self):
        queryset = Booking.objects.all()
        professional_id = self.request.query_params.get('professional_id', None)
        status_param = self.request.query_params.get('status', None)
        date = self.request.query_params.get('date', None)
        user_id = self.request.query_params.get('user_id', None)
        
        if professional_id:
            queryset = queryset.filter(professional_id=professional_id)
        if status_param:
            queryset = queryset.filter(status=status_param)
        if date:
            queryset = queryset.filter(date=date)
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        
        return queryset

    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        """Cancelar una reserva"""
        booking = self.get_object()
        
        if booking.status == 'cancelled':
            return Response(
                {'error': 'La reserva ya está cancelada'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        booking.status = 'cancelled'
        booking.save()
        
        # Liberar el horario
        Schedule.objects.filter(
            professional=booking.professional,
            date=booking.date,
            time=booking.time
        ).update(is_available=True)
        
        return Response({'status': 'Reserva cancelada exitosamente'})

    @action(detail=True, methods=['post'])
    def confirm(self, request, pk=None):
        """Confirmar una reserva"""
        booking = self.get_object()
        booking.status = 'confirmed'
        booking.save()
        return Response({'status': 'Reserva confirmada exitosamente'})

    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        """Marcar una reserva como completada"""
        booking = self.get_object()
        booking.status = 'completed'
        booking.save()
        return Response({'status': 'Reserva completada exitosamente'})

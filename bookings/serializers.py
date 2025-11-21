from rest_framework import serializers
from .models import Booking
from schedules.models import Schedule


class BookingSerializer(serializers.ModelSerializer):
    professional_name = serializers.CharField(source='professional.name', read_only=True)
    service_name = serializers.CharField(source='service.name', read_only=True)
    service_duration = serializers.IntegerField(source='service.duration', read_only=True)
    service_price = serializers.DecimalField(
        source='service.price',
        max_digits=10,
        decimal_places=2,
        read_only=True
    )

    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

    def validate(self, data):
        """Validar que el horario esté disponible"""
        if self.instance is None:  # Solo validar en creación
            professional = data.get('professional')
            date = data.get('date')
            time = data.get('time')
            
            # Verificar si existe un horario disponible
            try:
                schedule = Schedule.objects.get(
                    professional=professional,
                    date=date,
                    time=time,
                    is_available=True
                )
            except Schedule.DoesNotExist:
                raise serializers.ValidationError(
                    "El horario seleccionado no está disponible."
                )
            
            # Verificar que no haya otra reserva activa
            existing_booking = Booking.objects.filter(
                professional=professional,
                date=date,
                time=time,
                status__in=['pending', 'confirmed']
            ).exists()
            
            if existing_booking:
                raise serializers.ValidationError(
                    "Ya existe una reserva para este horario."
                )
        
        return data

    def create(self, validated_data):
        """Crear reserva y marcar horario como no disponible"""
        booking = super().create(validated_data)
        
        # Marcar el horario como no disponible
        Schedule.objects.filter(
            professional=booking.professional,
            date=booking.date,
            time=booking.time
        ).update(is_available=False)
        
        return booking


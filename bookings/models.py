from django.db import models
from django.contrib.auth.models import User
from professionals.models import Professional
from services.models import Service


class Booking(models.Model):
    """Reservas de servicios"""
    STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('confirmed', 'Confirmada'),
        ('cancelled', 'Cancelada'),
        ('completed', 'Completada'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='bookings',
        verbose_name='Usuario'
    )
    professional = models.ForeignKey(
        Professional,
        on_delete=models.CASCADE,
        related_name='bookings',
        verbose_name='Profesional'
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name='bookings',
        verbose_name='Servicio'
    )
    
    # Información del cliente
    client_name = models.CharField(max_length=200, verbose_name='Nombre del Cliente')
    client_email = models.EmailField(verbose_name='Email del Cliente')
    client_phone = models.CharField(max_length=20, verbose_name='Teléfono del Cliente')
    
    # Detalles de la reserva
    date = models.DateField(verbose_name='Fecha')
    time = models.TimeField(verbose_name='Hora')
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name='Estado'
    )
    notes = models.TextField(blank=True, verbose_name='Notas')
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Última Actualización')

    class Meta:
        ordering = ['-date', '-time']
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'

    def __str__(self):
        return f"{self.client_name} - {self.service.name} - {self.date}"

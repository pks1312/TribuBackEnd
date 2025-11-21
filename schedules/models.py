from django.db import models
from professionals.models import Professional


class Schedule(models.Model):
    """Horarios disponibles de los profesionales"""
    professional = models.ForeignKey(
        Professional,
        on_delete=models.CASCADE,
        related_name='schedules',
        verbose_name='Profesional'
    )
    date = models.DateField(verbose_name='Fecha')
    time = models.TimeField(verbose_name='Hora')
    is_available = models.BooleanField(default=True, verbose_name='Disponible')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Última Actualización')

    class Meta:
        ordering = ['date', 'time']
        unique_together = ['professional', 'date', 'time']
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'

    def __str__(self):
        return f"{self.professional.name} - {self.date} {self.time}"

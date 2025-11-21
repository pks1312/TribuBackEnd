from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from services.models import Service


class Testimonial(models.Model):
    """Testimonios de clientes"""
    author = models.CharField(max_length=200, verbose_name='Autor')
    content = models.TextField(verbose_name='Contenido')
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        default=5,
        verbose_name='Calificación'
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='testimonials',
        verbose_name='Servicio'
    )
    is_approved = models.BooleanField(default=False, verbose_name='Aprobado')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Última Actualización')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Testimonio'
        verbose_name_plural = 'Testimonios'

    def __str__(self):
        return f"{self.author} - {self.rating}★"

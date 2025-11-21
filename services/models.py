from django.db import models


class Service(models.Model):
    """Servicios ofrecidos por Tribu"""
    name = models.CharField(max_length=200, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripción')
    duration = models.IntegerField(help_text="Duración en minutos", verbose_name='Duración')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')
    image_url = models.URLField(blank=True, null=True, verbose_name='URL de Imagen')
    is_active = models.BooleanField(default=True, verbose_name='Activo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Última Actualización')

    class Meta:
        ordering = ['name']
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

    def __str__(self):
        return self.name

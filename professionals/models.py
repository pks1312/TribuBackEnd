from django.db import models


class Professional(models.Model):
    """Profesionales que ofrecen servicios"""
    name = models.CharField(max_length=200, verbose_name='Nombre')
    bio = models.TextField(blank=True, verbose_name='Biografía')
    photo_url = models.URLField(blank=True, null=True, verbose_name='Foto')
    specialties = models.TextField(help_text="Especialidades separadas por comas", verbose_name='Especialidades')
    is_active = models.BooleanField(default=True, verbose_name='Activo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Última Actualización')

    class Meta:
        ordering = ['name']
        verbose_name = 'Profesional'
        verbose_name_plural = 'Profesionales'

    def __str__(self):
        return self.name

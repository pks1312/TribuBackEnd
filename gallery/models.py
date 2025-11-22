from django.db import models


class GalleryImage(models.Model):
    """Imágenes de la galería"""
    title = models.CharField(max_length=200, blank=True, verbose_name='Título')
    description = models.TextField(blank=True, verbose_name='Descripción')
    # image = models.ImageField(upload_to='gallery/', verbose_name='Imagen')  # Requiere Pillow
    image_url = models.URLField(blank=True, null=True, verbose_name='URL de Imagen')
    category = models.CharField(max_length=100, blank=True, verbose_name='Categoría')
    is_active = models.BooleanField(default=True, verbose_name='Activo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Última Actualización')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Imagen de Galería'
        verbose_name_plural = 'Imágenes de Galería'

    def __str__(self):
        return self.title or f"Imagen {self.id}"

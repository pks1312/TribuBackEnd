from django.db import models
from django.contrib.auth.models import User

# Extendemos el modelo de usuario de Django con un perfil
class UserProfile(models.Model):
    """Perfil extendido de usuario"""
    ROLE_CHOICES = [
        ('admin', 'Administrador'),
        ('worker', 'Trabajador'),
        ('client', 'Cliente'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=20, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='client')
    photo_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Perfil de Usuario'
        verbose_name_plural = 'Perfiles de Usuario'

    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"


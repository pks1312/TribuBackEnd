#!/usr/bin/env python
"""
Script para actualizar el email del superusuario
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tribu_backend.settings')
django.setup()

from django.contrib.auth.models import User

def update_email():
    """Actualizar email del superusuario"""
    try:
        user = User.objects.get(username='pekita1312')
        user.email = 'sainttrentvto@mail.com'
        user.save()
        print(f"✅ Email actualizado para '{user.username}': {user.email}")
    except User.DoesNotExist:
        print("❌ Usuario 'pekita1312' no encontrado")

if __name__ == '__main__':
    update_email()


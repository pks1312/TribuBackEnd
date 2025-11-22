#!/usr/bin/env python
"""
Script para arreglar permisos de superusuario y crear datos de prueba
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tribu_backend.settings')
django.setup()

from django.contrib.auth.models import User
from accounts.models import UserProfile
from services.models import Service
from professionals.models import Professional

def fix_superuser():
    """Arreglar permisos del superusuario"""
    print("🔧 Arreglando permisos de superusuario...")
    
    # Buscar usuario pekita1312
    try:
        user = User.objects.get(username='pekita1312')
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()
        
        # Crear o actualizar perfil
        profile, created = UserProfile.objects.get_or_create(user=user)
        profile.role = 'admin'
        profile.save()
        
        print(f"✅ Usuario '{user.username}' ahora tiene permisos de staff y superusuario")
        print(f"✅ Rol del perfil: {profile.role}")
        
    except User.DoesNotExist:
        print("❌ Usuario 'pekita1312' no encontrado")
        print("🔧 Creando superusuario...")
        user = User.objects.create_superuser(
            username='pekita1312',
            email='sainttrentvto@mail.com',
            password='inacap2024.'
        )
        profile = UserProfile.objects.create(user=user, role='admin')
        print(f"✅ Superusuario creado: {user.username}")


def create_sample_data():
    """Crear datos de prueba"""
    print("\n📊 Creando datos de prueba...")
    
    # Crear servicios básicos
    services_data = [
        {
            'name': 'Corte de Cabello Caballero',
            'description': 'Corte de cabello profesional para caballeros',
            'price': 15000,
            'duration': 30,
            'active': True
        },
        {
            'name': 'Corte de Cabello Dama',
            'description': 'Corte de cabello profesional para damas',
            'price': 20000,
            'duration': 45,
            'active': True
        },
        {
            'name': 'Barba y Afeitado',
            'description': 'Servicio de barba y afeitado profesional',
            'price': 12000,
            'duration': 25,
            'active': True
        },
        {
            'name': 'Tinte',
            'description': 'Aplicación de tinte profesional',
            'price': 35000,
            'duration': 90,
            'active': True
        },
        {
            'name': 'Manicure',
            'description': 'Servicio de manicure completo',
            'price': 10000,
            'duration': 40,
            'active': True
        },
        {
            'name': 'Pedicure',
            'description': 'Servicio de pedicure completo',
            'price': 12000,
            'duration': 50,
            'active': True
        },
    ]
    
    for service_data in services_data:
        service, created = Service.objects.get_or_create(
            name=service_data['name'],
            defaults=service_data
        )
        if created:
            print(f"  ✅ Servicio creado: {service.name}")
        else:
            print(f"  ℹ️  Servicio ya existe: {service.name}")
    
    print(f"\n✅ Total de servicios en la base de datos: {Service.objects.count()}")


if __name__ == '__main__':
    print("=" * 60)
    print("🚀 SCRIPT DE CONFIGURACIÓN INICIAL")
    print("=" * 60)
    
    fix_superuser()
    create_sample_data()
    
    print("\n" + "=" * 60)
    print("✅ CONFIGURACIÓN COMPLETADA")
    print("=" * 60)
    print("\n📌 Ahora puedes:")
    print("  1. Entrar al admin: https://pekita1312.pythonanywhere.com/admin/")
    print("  2. Usuario: pekita1312")
    print("  3. Password: inacap2024.")
    print("=" * 60)


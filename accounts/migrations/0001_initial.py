# Generated manually

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='Teléfono')),
                ('address', models.TextField(blank=True, verbose_name='Dirección')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento')),
                ('profile_image_url', models.URLField(blank=True, null=True, verbose_name='URL de Imagen de Perfil')),
                ('is_professional', models.BooleanField(default=False, verbose_name='Es Profesional')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Última Actualización')),
                ('user', models.OneToOneField(on_delete=models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Perfil de Usuario',
                'verbose_name_plural': 'Perfiles de Usuario',
            },
        ),
    ]


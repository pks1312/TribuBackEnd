# Generated manually

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('phone', models.CharField(max_length=20, verbose_name='Teléfono')),
                ('bio', models.TextField(blank=True, verbose_name='Biografía')),
                ('profile_image_url', models.URLField(blank=True, null=True, verbose_name='URL de Imagen de Perfil')),
                ('specialties', models.TextField(blank=True, help_text='Separadas por coma', verbose_name='Especialidades')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Última Actualización')),
                ('services', models.ManyToManyField(blank=True, related_name='professionals', to='services.service', verbose_name='Servicios')),
            ],
            options={
                'verbose_name': 'Profesional',
                'verbose_name_plural': 'Profesionales',
                'ordering': ['name'],
            },
        ),
    ]


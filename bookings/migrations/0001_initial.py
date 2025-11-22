# Generated manually

from django.db import migrations, models
from django.conf import settings
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0001_initial'),
        ('professionals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateField(verbose_name='Fecha de Reserva')),
                ('booking_time', models.TimeField(verbose_name='Hora de Reserva')),
                ('status', models.CharField(choices=[('pending', 'Pendiente'), ('confirmed', 'Confirmada'), ('cancelled', 'Cancelada'), ('completed', 'Completada')], default='pending', max_length=20, verbose_name='Estado')),
                ('notes', models.TextField(blank=True, verbose_name='Notas')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Última Actualización')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bookings', to='services.service', verbose_name='Servicio')),
                ('professional', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bookings', to='professionals.professional', verbose_name='Profesional')),
            ],
            options={
                'verbose_name': 'Reserva',
                'verbose_name_plural': 'Reservas',
                'ordering': ['-booking_date', '-booking_time'],
            },
        ),
    ]


# Generated manually

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('professionals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.IntegerField(choices=[(0, 'Lunes'), (1, 'Martes'), (2, 'Miércoles'), (3, 'Jueves'), (4, 'Viernes'), (5, 'Sábado'), (6, 'Domingo')], verbose_name='Día de la Semana')),
                ('start_time', models.TimeField(verbose_name='Hora de Inicio')),
                ('end_time', models.TimeField(verbose_name='Hora de Fin')),
                ('is_available', models.BooleanField(default=True, verbose_name='Disponible')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Última Actualización')),
                ('professional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='professionals.professional', verbose_name='Profesional')),
            ],
            options={
                'verbose_name': 'Horario',
                'verbose_name_plural': 'Horarios',
                'ordering': ['professional', 'day_of_week', 'start_time'],
            },
        ),
    ]


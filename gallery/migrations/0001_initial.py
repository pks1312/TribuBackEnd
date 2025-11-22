# Generated manually

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, verbose_name='Título')),
                ('description', models.TextField(blank=True, verbose_name='Descripción')),
                ('image_url', models.URLField(blank=True, null=True, verbose_name='URL de Imagen')),
                ('category', models.CharField(blank=True, max_length=100, verbose_name='Categoría')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Última Actualización')),
            ],
            options={
                'verbose_name': 'Imagen de Galería',
                'verbose_name_plural': 'Imágenes de Galería',
                'ordering': ['-created_at'],
            },
        ),
    ]


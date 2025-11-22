# Generated manually to add role field

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='role',
            field=models.CharField(
                choices=[('admin', 'Administrador'), ('worker', 'Trabajador'), ('client', 'Cliente')],
                default='client',
                max_length=20
            ),
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='address',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='is_professional',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='profile_image_url',
            new_name='photo_url',
        ),
    ]


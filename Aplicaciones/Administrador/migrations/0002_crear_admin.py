from django.db import migrations
from django.contrib.auth.hashers import make_password

def crear_admin(apps, schema_editor):
    Administrador = apps.get_model('Administrador', 'Administrador')
    if not Administrador.objects.filter(user='adminmo').exists():
        Administrador.objects.create(
            user='adminmo',
            passwo=make_password('inmo0708')
        )

class Migration(migrations.Migration):

    dependencies = [
        ('Administrador', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(crear_admin),
    ]

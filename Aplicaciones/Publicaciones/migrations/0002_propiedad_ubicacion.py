# Generated by Django 5.2 on 2025-07-14 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Publicaciones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='propiedad',
            name='ubicacion',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

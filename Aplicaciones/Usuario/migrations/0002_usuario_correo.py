# Generated by Django 5.2 on 2025-06-28 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='correo',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
    ]

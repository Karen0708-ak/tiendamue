from django.db import models

class Usuario(models.Model):
    usuario = models.CharField(max_length=150, unique=True)
    contrasena = models.CharField(max_length=128)
    correo = models.EmailField(unique=True,null=True, blank=True)
    telefono = models.CharField(null=True, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    telegram_id = models.CharField(max_length=50, null=True, blank=True)

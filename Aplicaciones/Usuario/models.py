from django.db import models

class Usuario(models.Model):
    usuario = models.CharField(max_length=150, unique=True)
    contrasena = models.CharField(max_length=128)
    correo = models.EmailField(unique=True,null=True, blank=True)

from django.db import models

class Denuncia(models.Model):
    motivo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    

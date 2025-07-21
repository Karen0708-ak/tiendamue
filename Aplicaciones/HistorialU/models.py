from django.db import models

# Create your models here.
from django.db import models
from Aplicaciones.Usuario.models import Usuario 

class HistorialUsuario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='historial')
    accion = models.CharField(max_length=100)  
    descripcion = models.TextField()        
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.usuario} - {self.accion}"

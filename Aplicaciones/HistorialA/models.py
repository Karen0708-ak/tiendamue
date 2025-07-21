from django.db import models

# Create your models here.
from django.db import models
from Aplicaciones.Administrador.models import Administrador 

class HistorialAdmin(models.Model):
    administrador = models.ForeignKey(Administrador, on_delete=models.CASCADE, related_name='historialA')
    accion = models.CharField(max_length=100)  
    descripcion = models.TextField()        
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.administrador.user} - {self.accion}"

from django.db import models
from Aplicaciones.Usuario.models import Usuario
from Aplicaciones.Publicaciones.models import Propiedad

# Create your models here.
class Interez(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE)
    fecha_interes = models.DateTimeField(auto_now_add=True)
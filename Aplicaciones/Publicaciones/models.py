from django.db import models
from Aplicaciones.Usuario.models import Usuario

class Propiedad(models.Model):
    id_propiedad = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='propiedades/')
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=12, decimal_places=2)  # Mantén solo este
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    latitud = models.DecimalField(max_digits=9, decimal_places=7)
    longitud = models.DecimalField(max_digits=10, decimal_places=7)
    estado = models.CharField(max_length=50)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

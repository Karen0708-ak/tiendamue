from django.db import models
from Aplicaciones.Usuario.models import Usuario
from Aplicaciones.Publicaciones.models import Propiedad

class Comentario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE)
    comentario = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario.usuario} - {self.propiedad.titulo}'
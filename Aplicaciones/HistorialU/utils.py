from .models import HistorialUsuario
from Aplicaciones.Usuario.models import Usuario

def registrar_historial(request, accion, descripcion):
    usuario_actual = Usuario.objects.get(id=request.session['usuario_id'])
    HistorialUsuario.objects.create(
        usuario=usuario_actual,
        accion=accion,
        descripcion=descripcion
    )

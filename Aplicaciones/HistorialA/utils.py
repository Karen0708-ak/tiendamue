from .models import HistorialAdmin
from Aplicaciones.Administrador.models import Administrador

def registrar_historial_admin(request, accion, descripcion):
    admin_id = request.session.get('admin_id')
    if admin_id:
        admin_actual = Administrador.objects.get(id=admin_id)
        HistorialAdmin.objects.create(
            administrador=admin_actual,
            accion=accion,
            descripcion=descripcion
        )
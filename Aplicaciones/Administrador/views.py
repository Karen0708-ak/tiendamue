from django.shortcuts import render,redirect
from Aplicaciones.Publicaciones.models import Propiedad
from Aplicaciones.Usuario.models import Usuario
from .models import Administrador
from Aplicaciones.HistorialA.utils import registrar_historial_admin
# Create your views here.
def admiin(request):
    if 'admin_id' not in request.session:
        return redirect('iniciosesion')
    propiedades = Propiedad.objects.select_related('usuario').all()
    return render(request, 'admiin.html', {'propiedades': propiedades})

##############LISTA DE USUARIOS############
def usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})

############Eliminar publicacion por denuncia###########
from django.shortcuts import get_object_or_404, redirect
from Aplicaciones.Notificacion.models import Notificacion
from django.contrib import messages

def eliminar_propiedad(request, id_propiedad):
    if 'admin_id' not in request.session:
        messages.error(request, 'Debes iniciar sesión como administrador.')
        return redirect('iniciosesion')

    propiedad = get_object_or_404(Propiedad, pk=id_propiedad)
    usuario = propiedad.usuario  


    mensaje = f'Tu publicación "{propiedad.titulo}" fue eliminada por el administrador debido a denuncias.'
    Notificacion.objects.create(
        usuario=usuario,
        mensaje=mensaje,
    )

    propiedad.delete()
    messages.success(request, 'Propiedad eliminada y usuario notificado correctamente.')
    admin = Administrador.objects.get(id=request.session['admin_id'])
    registrar_historial_admin(
        request,
        "Eliminar propiedad",
        f"Eliminaste la propiedad '{propiedad.titulo}."
    )
    return redirect('admiin')

from django.shortcuts import render, redirect
from Aplicaciones.HistorialU.models import HistorialUsuario

def historialusuarios(request):
    historial = HistorialUsuario.objects.select_related('usuario').all().order_by('-fecha')

    return render(request, 'historialusuarios.html', {'historial': historial})

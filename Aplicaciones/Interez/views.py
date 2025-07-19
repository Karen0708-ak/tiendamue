from django.shortcuts import redirect, get_object_or_404,render
from Aplicaciones.Interez.models import Interez
from Aplicaciones.Publicaciones.models import Propiedad
from Aplicaciones.Usuario.models import Usuario
from django.contrib import messages

def registrar_interes(request, propiedad_id):
    if 'usuario_id' not in request.session:
        messages.error(request, "Debes iniciar sesión para guardar intereses.")
        return redirect('iniciosesion')

    propiedad = get_object_or_404(Propiedad, id_propiedad=propiedad_id)
    usuario = get_object_or_404(Usuario, id=request.session['usuario_id'])

    if not Interez.objects.filter(usuario=usuario, propiedad=propiedad).exists():
        Interez.objects.create(usuario=usuario, propiedad=propiedad)
        messages.success(request, "Se intereso por esta propiedad.")
    else:
        messages.info(request, "Ya habías registrado tu interés por esta propiedad.")

    return redirect('publicacion', id_propiedad=propiedad.id_propiedad)


def intereses(request):
    intereses = Interez.objects.select_related('usuario', 'propiedad').all()
    return render(request, 'intereses.html', {'intereses': intereses})


def eliminarinterez(request, interes_id):
    interes = get_object_or_404(Interez, id=interes_id)

    if request.session.get('usuario_id') != interes.usuario.id:
        messages.error(request, "No tienes permiso para eliminar este interés.")
        return redirect('intereses')

    interes.delete()
    messages.success(request, "Interés eliminado correctamente.")
    return redirect('intereses')
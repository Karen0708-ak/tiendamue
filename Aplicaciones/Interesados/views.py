from django.shortcuts import render,redirect

# Create your views here.

from Aplicaciones.Usuario.models import Usuario
from Aplicaciones.Publicaciones.models import Propiedad
from Aplicaciones.Interez.models import Interez



def interesados_en_mis_publicaciones(request):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('iniciosesion') 

    usuario_actual = Usuario.objects.get(id=usuario_id)
    mis_publicaciones = Propiedad.objects.filter(usuario=usuario_actual)
    intereses = Interez.objects.filter(propiedad__in=mis_publicaciones).select_related('usuario', 'propiedad')

    return render(request, 'lista.html', {'intereses': intereses})
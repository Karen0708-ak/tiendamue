from django.shortcuts import render,redirect

# Create your views here.
from Aplicaciones.Usuario.models import Usuario

def mihistorial(request):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        # Usuario no autenticado lo redirige al inicio
        return redirect('iniciosesion')

    usuario = Usuario.objects.get(id=usuario_id)
    historial = usuario.historial.all().order_by('-fecha')  

    return render(request, 'mihistorial.html', {'historial': historial})
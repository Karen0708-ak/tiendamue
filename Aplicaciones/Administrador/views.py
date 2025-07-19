from django.shortcuts import render,redirect

from Aplicaciones.Usuario.models import Usuario
# Create your views here.
def admiin(request):
    if 'admin_id' not in request.session:
        return redirect('iniciosesion')
    return render(request, 'admiin.html')

##############LISTA DE USUARIOS############
def usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})
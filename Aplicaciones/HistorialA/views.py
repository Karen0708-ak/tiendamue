from django.shortcuts import render,redirect

# Create your views here.
from Aplicaciones.Administrador.models import Administrador

def adminhistorial(request):
    admin_id = request.session.get('admin_id')
    if not admin_id:
        return redirect('iniciosesion')

    usuario = Administrador.objects.get(id=admin_id)
    historial = usuario.historialA.all().order_by('-fecha')  

    return render(request, 'adminhistorial.html', {'historial': historial})
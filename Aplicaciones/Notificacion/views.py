from django.shortcuts import render,redirect
from Aplicaciones.Usuario.models import Usuario
from .models import Notificacion
from django.http import JsonResponse


# Create your views here.

def notificaciones(request):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('iniciosesion')

    usuario = Usuario.objects.get(id=usuario_id)
    notificaciones = Notificacion.objects.filter(usuario=usuario).order_by('-fecha')

    return render(request, 'notificaciones.html', {'notificaciones': notificaciones})

def obtener_notificaciones_nuevas(request):
    usuario_id = request.session.get('usuario_id')
    if usuario_id:
        notificaciones = Notificacion.objects.filter(usuario_id=usuario_id, leido=False)
        data = []
        for n in notificaciones:
            data.append({
                'id': n.id,
                'mensaje': n.mensaje,
                'fecha': n.fecha.strftime("%d-%m-%Y %H:%M")
            })
            n.leido = True
            n.save()
        return JsonResponse({'notificaciones': data})
    return JsonResponse({'notificaciones': []})
from django.shortcuts import render, redirect, get_object_or_404
from .models import Comentario
from Aplicaciones.Publicaciones.models import Propiedad
from Aplicaciones.Usuario.models import Usuario
from django.http import JsonResponse
from django.utils import timezone
from Aplicaciones.HistorialU.utils import registrar_historial
from django.contrib import messages

# Create your views here.

def agregar_comentario(request, id_propiedad):
    if request.method == 'POST':
        texto_comentario = request.POST.get('comentario')
        comentario = request.POST.get('comentario')
        propiedad = get_object_or_404(Propiedad, id_propiedad=id_propiedad)
        usuario = get_object_or_404(Usuario, id=request.session.get('usuario_id'))

        comentario = Comentario.objects.create(
            propiedad=propiedad,
            usuario=usuario,
            comentario=comentario,
            fecha=timezone.now()
        )
        registrar_historial(
            request,
            "Comentario creado",
            f"Comentó en la propiedad '{propiedad.titulo}': \"{texto_comentario[:50]}\""
        )

        return JsonResponse({
            'success': True,
            'comentario': comentario.comentario,
            'usuario': usuario.usuario 
        })
    
    return JsonResponse({'success': False}, status=400)
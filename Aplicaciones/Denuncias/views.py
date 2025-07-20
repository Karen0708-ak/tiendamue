from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Denuncia

def registrar_denuncia(request, id_propiedad):
    if request.method == 'POST':
        motivo = request.POST.get('motivo')
        descripcion = request.POST.get('descripcion', '')
        
        # Guardar la denuncia en la base de datos
        denuncia = Denuncia.objects.create(
            motivo=motivo,
            descripcion=descripcion
        )
        
        # Enviar correo electrónico
        asunto = f"Nueva denuncia recibida: {motivo}"
        mensaje = f"""
        Se ha recibido una nueva denuncia:
        
        Motivo: {motivo}
        Descripción: {descripcion}
        
        ID de Propiedad: {id_propiedad}
        """
        
        send_mail(
            asunto,
            mensaje,
            settings.EMAIL_HOST_USER,  # Remitente
            ['barciakaren655@gmail.com'],  # Destinatario
            fail_silently=False,
        )
        
        messages.success(request, 'Denuncia enviada correctamente. Gracias por tu reporte.')
        return redirect('inicio')
    
    return render(request, 'denuncias/denuncia_modal.html')
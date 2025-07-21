from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from Aplicaciones.Publicaciones.models import Propiedad
from .models import Denuncia
from Aplicaciones.HistorialU.utils import registrar_historial

def registrar_denuncia(request, id_propiedad):
    if request.method == 'POST':
        motivo = request.POST.get('motivo')
        descripcion = request.POST.get('descripcion', '')

        propiedad = get_object_or_404(Propiedad, id_propiedad=id_propiedad)
        usuario = None
        if 'usuario_id' in request.session:
            from Aplicaciones.Usuario.models import Usuario
            usuario = Usuario.objects.get(id=request.session['usuario_id'])
        
        # Guardar la denuncia en la base de datos
        denuncia = Denuncia.objects.create(
            motivo=motivo,
            descripcion=descripcion
        )
        if 'usuario_id' in request.session:
            usuario = get_object_or_404(Usuario, id=request.session['usuario_id'])
            registrar_historial(
                request,
                "Registro de denuncia",
                f"Registró una denuncia para la propiedad '{propiedad.titulo}' con motivo: {motivo}"
            )
        
        # Enviar correo electrónico
        asunto = f"Nueva denuncia recibida: {motivo}- {propiedad.titulo}"
        mensaje = f"""
        Se ha recibido una nueva denuncia:

        Propiedad: {propiedad.titulo}
        Motivo: {motivo}
        Descripción: {descripcion}
        

        """
        
        send_mail(
            asunto,
            mensaje,
            settings.EMAIL_HOST_USER,  # Remitente
            ['barciakaren655@gmail.com'],  # Destinatario
            fail_silently=False,
        )
        
        messages.success(request, 'Denuncia enviada correctamente. Gracias por tu reporte.')
        return redirect('inicios')
    
    return render(request, 'denuncias/denuncia_modal.html')
from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from Aplicaciones.Administrador.models import Administrador
from Aplicaciones.Publicaciones.models import Propiedad
from django.http import JsonResponse
from Aplicaciones.Notificacion.models import Notificacion

def index(request):
    usuario = Usuario.objects.all()
    return render(request, 'index.html')
def inicio(request):
    propiedades = Propiedad.objects.all().order_by('-fecha_publicacion')
    usuario_id = request.session.get('usuario_id')
    
    total_notificaciones = 0
    if usuario_id:
        total_notificaciones = Notificacion.objects.filter(usuario_id=usuario_id, leido=False).count()
    return render(request, 'inicios.html', {'propiedades': propiedades,'usuario_id': usuario_id,'total_notificaciones': total_notificaciones})


def nuevoUsuario(request):
    return render(request, "nuevoUsuario.html")

def guardaregistro(request):
    if request.method == 'POST':
        usuario = request.POST['usuario']
        correo = request.POST['correo']
        contrasena = request.POST['contrasena']
        telefono = request.POST['telefono']


        if Usuario.objects.filter(usuario=usuario).exists():
            messages.error(request, 'El nombre de usuario ya está en uso.')
            return redirect('nuevoUsuario')

        if Usuario.objects.filter(correo=correo).exists():
            messages.error(request, 'El correo ya está registrado.')
            return redirect('nuevoUsuario')


        contrasena_encriptada = make_password(contrasena)

        Usuario.objects.create(
            usuario=usuario,
            correo=correo,
            contrasena=contrasena_encriptada,
            telefono=telefono,
        )

        messages.success(request, '¡Usuario registrado exitosamente!')
        return redirect('iniciosesion')
    

def iniciosesion(request):
    if request.method == 'POST':
   
        input_usuario = request.POST.get('usuario')
        input_contrasena = request.POST.get('contrasena')

        # administrador 
        try:
            admin = Administrador.objects.get(user=input_usuario)
            if check_password(input_contrasena, admin.passwo):
                request.session['admin_id'] = admin.id
                messages.success(request, '¡Bienvenido!')
                return redirect('admiin')
        except Administrador.DoesNotExist:
            pass

        #usuario
        try:
            usuario = Usuario.objects.get(usuario=input_usuario)
            if check_password(input_contrasena, usuario.contrasena):
                request.session['usuario_id'] = usuario.id
                request.session['usuario_nombre'] = usuario.usuario
                messages.success(request, '¡Bienvenido!')
                return redirect('inicios')
            else:
                messages.error(request, 'Contraseña incorrecta.')
        except Usuario.DoesNotExist:
            messages.error(request, 'El usuario no existe.')

    return render(request, 'iniciosesion.html')
def cerrarsesion(request):
    request.session.flush()  
    messages.success(request, 'Sesión cerrada correctamente.')
    return redirect('iniciosesion')

def perfil_usuario(request):
    if 'usuario_id' not in request.session:
        return JsonResponse({'error': 'Usuario no autenticado'}, status=401)

    usuario = Usuario.objects.get(id=request.session['usuario_id'])

    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        usuario.usuario = request.POST.get('usuario')
        usuario.correo = request.POST.get('correo')
        usuario.telefono = request.POST.get('telefono')
        nueva_contrasena = request.POST.get('contrasena')

        if nueva_contrasena:
            usuario.contrasena = make_password(nueva_contrasena)

        usuario.save()
        return JsonResponse({'success': True, 'message': 'Datos actualizados correctamente'})

    return render(request, 'perfil.html', {'usuario': usuario})

###############PROPIEDAD#########

def detalle_propiedad(request, id_propiedad):
    propiedad = get_object_or_404(Propiedad, pk=id_propiedad)
    usuario = propiedad.usuario
    return render(request, 'publicacion.html', {
        'propiedad': propiedad,
        'usuario': usuario
    })
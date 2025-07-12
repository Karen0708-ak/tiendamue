from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from Aplicaciones.Administrador.models import Administrador

def index(request):
    usuario = Usuario.objects.all()
    return render(request, 'index.html')
def inicio(request):
    inicio=Usuario.objects.all()
    return render(request, 'inicios.html')

def nuevoUsuario(request):
    return render(request, "nuevoUsuario.html")

def guardaregistro(request):
    if request.method == 'POST':
        usuario = request.POST['usuario']
        correo = request.POST['correo']
        contrasena = request.POST['contrasena']

        # Validar existencia previa
        if Usuario.objects.filter(usuario=usuario).exists():
            messages.error(request, 'El nombre de usuario ya está en uso.')
            return redirect('nuevoUsuario')

        if Usuario.objects.filter(correo=correo).exists():
            messages.error(request, 'El correo ya está registrado.')
            return redirect('nuevoUsuario')

        # Encriptar y guardar
        contrasena_encriptada = make_password(contrasena)

        Usuario.objects.create(
            usuario=usuario,
            correo=correo,
            contrasena=contrasena_encriptada
        )

        messages.success(request, '¡Usuario registrado exitosamente!')
        return redirect('index')
    
    return redirect('index')

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
                return redirect('admin_panel')
        except Administrador.DoesNotExist:
            pass

        #usuario
        try:
            usuario = Usuario.objects.get(usuario=input_usuario)
            if check_password(input_contrasena, usuario.contrasena):
                request.session['usuario_id'] = usuario.id
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
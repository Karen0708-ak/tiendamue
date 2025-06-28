from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario
from django.contrib.auth.hashers import make_password
from django.contrib import messages

def index(request):
    usuario = Usuario.objects.all()
    return render(request, 'index.html')
def inicio(request):
    inicio=Usuario.objects.all()
    return render(request, 'inicios.html')

def nuevoUsuario(request):
    return render(request, "nuevoUsuario.html")

def guardaregistro(request):
    mensaje = ''
    if request.method == 'POST':
        usuario = request.POST['usuario']
        correo = request.POST['correo']  # Nuevo dato
        contrasena = request.POST['contrasena']

        contrasena_encriptada = make_password(contrasena)

        try:
            Usuario.objects.create(
                usuario=usuario,
                correo=correo,
                contrasena=contrasena_encriptada
            )
            mensaje = '¡Registro exitoso!'
        except:
            mensaje = 'Error: el usuario o correo ya existe'
    messages.success(request, "Usuario registrado exitosamente")
    return redirect('index')

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from Aplicaciones.Usuario.models import Usuario
from .models import Propiedad

def inicio(request):
    usuario_actual = Usuario.objects.get(id=request.session['usuario_id']) 
    listado_propiedades = Propiedad.objects.filter(usuario=usuario_actual)
    return render(request, "iniciopu.html", {'propiedades': listado_propiedades})


def nuevaPropiedad(request):
    return render(request, "nuevaPropiedad.html")

def guardarPropiedad(request):
    if request.method == "POST":
        titulo = request.POST["titulo"]
        descripcion = request.POST["descripcion"]
        precio = request.POST["precio"].replace(',', '.')
        ubicacion = request.POST["ubicacion"]
        latitud = request.POST["latitud"]
        longitud = request.POST["longitud"]
        estado = request.POST["estado"]
        imagen = request.FILES.get("imagen")

        usuario_actual = Usuario.objects.get(id=request.session['usuario_id'])

        Propiedad.objects.create(
            titulo=titulo,
            descripcion=descripcion,
            precio=precio,
            ubicacion=ubicacion,
            latitud=latitud,
            longitud=longitud,
            estado=estado,
            imagen=imagen,
            usuario=usuario_actual
        )

        messages.success(request, "Propiedad guardada exitosamente")
        return redirect('iniciopu')

def eliminarPropiedad(request, id):
    propiedad = get_object_or_404(Propiedad, id_propiedad=id)
    propiedad.delete()
    messages.success(request, "Propiedad eliminada exitosamente")
    return redirect('iniciopu')

def editarPropiedad(request, id):
    propiedad = get_object_or_404(Propiedad, id_propiedad=id)
    return render(request, "editarPropiedad.html", {'propiedad': propiedad})


def procesarEdicionPropiedad(request):
    if request.method == "POST":
        id = request.POST["id"]
        titulo = request.POST["titulo"]
        descripcion = request.POST["descripcion"]
        precio = request.POST["precio"].replace(',', '.')
        ubicacion=request.POST["ubicacion"]
        latitud = request.POST["latitud"].replace(',', '.').replace('“', '').replace('”', '').strip()
        longitud = request.POST["longitud"].replace(',', '.').replace('“', '').replace('”', '').strip()
        estado = request.POST["estado"]
        imagen_nueva = request.FILES.get("imagen")

        propiedad = get_object_or_404(Propiedad, id_propiedad=id)
        propiedad.titulo = titulo
        propiedad.descripcion = descripcion
        propiedad.precio = precio
        propiedad.ubicacion=ubicacion
        propiedad.latitud = latitud
        propiedad.longitud = longitud
        propiedad.estado = estado

        if imagen_nueva:
            propiedad.imagen = imagen_nueva

        propiedad.save()
        messages.success(request, "Propiedad actualizada exitosamente")
        return redirect('iniciopu')

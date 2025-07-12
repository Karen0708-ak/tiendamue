from django.shortcuts import render, redirect, get_object_or_404
from .models import Propiedad
from Aplicaciones.Usuario.models import Usuario 
# Create your views here.

def inicio(request):
    publicaciones = Propiedad.objects.all()
    return render(request, 'publicaciones.html')
from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario

def index(request):
    usuario = Usuario.objects.all()
    return render(request, 'index.html')
def inicio(request):
    inicio=Usuario.objects.all()
    return render(request, 'inicios.html')
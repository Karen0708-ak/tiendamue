from django.shortcuts import render
from .models import Administrador
# Create your views here.
def inicio(request):
    inicio=Administrador.objects.all()
    return render(request, 'admin.html')
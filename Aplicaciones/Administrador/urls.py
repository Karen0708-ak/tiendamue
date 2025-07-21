from django.urls import path
from . import views

urlpatterns = [
    path('admiin', views.admiin, name='admiin'),
    path('eliminar_propiedad/<id_propiedad>', views.eliminar_propiedad, name='eliminar_propiedad'),
    path('usuarios', views.usuarios, name='usuarios'),
    path('historialusuarios', views.historialusuarios, name='historialusuarios'),
]
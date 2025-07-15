from django.urls import path
from . import views

urlpatterns = [
    path('iniciopu',views.inicio,name='iniciopu'),
    path('nuevaPropiedad',views.nuevaPropiedad),
    path('guardarPropiedad',views.guardarPropiedad),
    path('eliminarPropiedad/<id>',views.eliminarPropiedad),
    path('editarPropiedad/<id>',views.editarPropiedad),
    path('procesarEdicionPropiedad', views.procesarEdicionPropiedad, name='procesarEdicionPropiedad'),

]
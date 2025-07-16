from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('inicios', views.inicio, name='inicios'),
    path('nuevoUsuario',views.nuevoUsuario,name='nuevoUsuario'),
    path('guardaregistro', views.guardaregistro,name='guardaregistro'),
    path('iniciosesion', views.iniciosesion,name='iniciosesion'),
    path('cerrarsesion', views.cerrarsesion,name='cerrarsesion'),
    path('publicacion/<id_propiedad>', views.detalle_propiedad,name='publicacion'),



]
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('inicios', views.inicio, name='inicios'),
    path('nuevoUsuario',views.nuevoUsuario,name='nuevoUsuario'),
    path('guardaregistro', views.guardaregistro,name='guardaregistro'),
]
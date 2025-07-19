from django.urls import path
from . import views

urlpatterns = [
    path('notificaciones', views.notificaciones, name='notificaciones'),
    path('nuevas', views.obtener_notificaciones_nuevas, name='notificaciones_nuevas'),
]
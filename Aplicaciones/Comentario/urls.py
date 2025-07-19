from django.urls import path
from . import views
urlpatterns = [
    path('agregar_comentario/<id_propiedad>/', views.agregar_comentario, name='agregar_comentario'),
    
]
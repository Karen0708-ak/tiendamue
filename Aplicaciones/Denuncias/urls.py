from django.urls import path
from . import views

urlpatterns = [
    path('registrar/<int:id_propiedad>/', views.registrar_denuncia, name='registrar_denuncia'),
]

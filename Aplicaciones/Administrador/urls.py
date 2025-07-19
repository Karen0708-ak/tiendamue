from django.urls import path
from . import views

urlpatterns = [
    path('admiin', views.admiin, name='admiin'),
    path('usuarios', views.usuarios, name='usuarios'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('mis-interesados', views.interesados_en_mis_publicaciones, name='mis_interesados'),
]

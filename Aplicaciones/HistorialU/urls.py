from django.urls import path
from . import views

urlpatterns = [
    path('mihistorial', views.mihistorial, name='mihistorial'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('adminhistorial', views.adminhistorial, name='adminhistorial'),
]
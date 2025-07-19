from django.urls import path
from . import views

urlpatterns = [
    path('registrar/<int:propiedad_id>', views.registrar_interes, name='registrar_interes'),
    path('intereses', views.intereses, name='intereses'),
    path('eliminarinterez/<interes_id>', views.eliminarinterez, name='eliminarinterez'),

]

"""
URL configuration for tiendamue project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.views.generic import RedirectView
from django.urls import reverse_lazy

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('index'), permanent=False)), 
    path('admin/', admin.site.urls),
    path('Usuario/', include('Aplicaciones.Usuario.urls')),
    path('Publicaciones/', include('Aplicaciones.Publicaciones.urls')),
    path('Administrador/', include('Aplicaciones.Administrador.urls')),
    path('Interez/', include('Aplicaciones.Interez.urls')),
    path('Comentario/', include('Aplicaciones.Comentario.urls')),
    path('Interesados/', include('Aplicaciones.Interesados.urls')),
    path('Notificacion/', include('Aplicaciones.Notificacion.urls')),
    path('Denuncias/', include('Aplicaciones.Denuncias.urls')),
    path('HistorialU/', include('Aplicaciones.HistorialU.urls')),
    path('HistorialA/', include('Aplicaciones.HistorialA.urls')),

]
if settings.DEBUG:urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
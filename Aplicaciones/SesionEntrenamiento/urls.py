from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicioSesion, name='indexSesion'),  
    path('nuevaSesion', views.nuevaSesion, name='nuevaSesion'),  
    path('guardarSesion', views.guardarSesion, name='guardarSesion'), 
    path('eliminarSesion/<id>', views.eliminarSesion, name='eliminarSesion'),  
    path('editarSesion/<id>', views.editarSesion, name='editarSesion'),  
    path('procesarEdicionSesion/<id>', views.procesarEdicionSesion, name='procesarEdicionSesion'),  
]

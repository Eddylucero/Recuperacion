from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicioAdiestrador, name='indexAdiestrador'),
    path('nuevoAdiestrador', views.nuevoAdiestrador, name='nuevoAdiestrador'),
    path('guardarAdiestrador', views.guardarAdiestrador, name='guardarAdiestrador'),
    path('eliminarAdiestrador/<id>', views.eliminarAdiestrador, name='eliminarAdiestrador'),
    path('editarAdiestrador/<id>', views.editarAdiestrador, name='editarAdiestrador'),
    path('procesarEdicionAdiestrador/<id>', views.procesarEdicionAdiestrador, name='procesarEdicionAdiestrador'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicioPerro, name='indexPerro'),
    path('nuevoPerro', views.nuevoPerro, name='nuevoPerro'),
    path('guardarPerro', views.guardarPerro, name='guardarPerro'),
    path('eliminarPerro/<id>', views.eliminarPerro, name='eliminarPerro'),
    path('editarPerro/<id>', views.editarPerro, name='editarPerro'),
    path('procesarEdicionPerro/<id>', views.procesarEdicionPerro, name='procesarEdicionPerro'),
]

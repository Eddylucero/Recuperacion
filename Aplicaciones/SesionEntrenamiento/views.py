from django.shortcuts import render, redirect
from .models import SesionEntrenamiento
from .models import PerroDetector
from .models import AdiestradorAgricola
from django.contrib import messages

def inicioSesion(request):
    listadoSesiones = SesionEntrenamiento.objects.all()
    return render(request, "SesionesEntrenamiento/inicioSesion.html", {'sesiones': listadoSesiones})

def nuevaSesion(request):
    perros = PerroDetector.objects.all()
    adiestradores = AdiestradorAgricola.objects.all()
    return render(request, "SesionesEntrenamiento/nuevaSesion.html", {"perros": perros, "adiestradores": adiestradores})

def guardarSesion(request):
    if request.method == "POST":
        fecha = request.POST["fecha"]
        duracion = request.POST["duracion"]
        resultado = request.POST["resultado"]
        perro_id = request.POST["perro"]
        adiestrador_id = request.POST["adiestrador"]

        perro = PerroDetector.objects.get(id=perro_id)
        adiestrador = AdiestradorAgricola.objects.get(id=adiestrador_id)

        SesionEntrenamiento.objects.create(fecha=fecha, duracion=duracion, resultado=resultado, perro=perro, adiestrador=adiestrador)
        messages.success(request, "SE HA AGREGADO EL NUEVO SESION DE ENTRENAMIENTO")

        return redirect('indexSesion')
    return redirect('indexSesion')

def eliminarSesion(request, id):
    sesionEliminar = SesionEntrenamiento.objects.get(id=id)
    sesionEliminar.delete()
    messages.success(request, "SE HA ELIMINADO LA SESION DE ENTRENAMIENTO")
    return redirect('indexSesion')

def editarSesion(request, id):
    sesion = SesionEntrenamiento.objects.get(id=id)
    perros = PerroDetector.objects.all()
    adiestradores = AdiestradorAgricola.objects.all()
    return render(request, "SesionesEntrenamiento/editarSesion.html", {"sesion": sesion, "perros": perros, "adiestradores": adiestradores})

def procesarEdicionSesion(request, id):
    fecha = request.POST["fecha"]
    duracion = request.POST["duracion"]
    resultado = request.POST["resultado"]
    perro_id = request.POST["perro"]
    adiestrador_id = request.POST["adiestrador"]

    sesion = SesionEntrenamiento.objects.get(id=id)
    perro = PerroDetector.objects.get(id=perro_id)
    adiestrador = AdiestradorAgricola.objects.get(id=adiestrador_id)

    sesion.fecha = fecha
    sesion.duracion = duracion
    sesion.resultado = resultado
    sesion.perro = perro
    sesion.adiestrador = adiestrador
    sesion.save()
    messages.success(request, "SE HA EDITADO LA SESION DE ENTRENAMIENTO")

    return redirect('indexSesion')

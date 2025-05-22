from django.shortcuts import render, redirect
from .models import AdiestradorAgricola
from django.contrib import messages

def inicioAdiestrador(request):
    listadoAdiestradores = AdiestradorAgricola.objects.all()
    return render(request, "AdiestradoresAgricolas/inicioAdiestrador.html", {'adiestradores': listadoAdiestradores})

def nuevoAdiestrador(request):
    return render(request, "AdiestradoresAgricolas/nuevoAdiestrador.html")

def guardarAdiestrador(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        especialidad = request.POST["especialidad"]
        experiencia = request.POST["experiencia"]

        AdiestradorAgricola.objects.create(nombre=nombre, especialidad=especialidad, experiencia=experiencia)
        messages.success(request, "SE HA AGREGADO EL NUEVO ADIESTRADOR AGRÍCOLA")

        return redirect('indexAdiestrador')
    return redirect('indexAdiestrador')

def eliminarAdiestrador(request, id):
    adiestradorEliminar = AdiestradorAgricola.objects.get(id=id)
    adiestradorEliminar.delete()
    messages.success(request, "SE HA ELIMINADO EL ADIESTRADOR AGRÍCOLA")
    return redirect('indexAdiestrador')

def editarAdiestrador(request, id):
    adiestrador = AdiestradorAgricola.objects.get(id=id)
    return render(request, "AdiestradoresAgricolas/editarAdiestrador.html", {'adiestrador': adiestrador})

def procesarEdicionAdiestrador(request, id):
    nombre = request.POST["nombre"]
    especialidad = request.POST["especialidad"]
    experiencia = request.POST["experiencia"]

    adiestrador = AdiestradorAgricola.objects.get(id=id)
    adiestrador.nombre = nombre
    adiestrador.especialidad = especialidad
    adiestrador.experiencia = experiencia
    adiestrador.save()
    messages.success(request, "SE HA EDITADO EL ADIESTRADOR AGRÍCOLA")

    return redirect('indexAdiestrador')

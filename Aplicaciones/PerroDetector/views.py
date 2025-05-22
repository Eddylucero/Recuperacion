from django.shortcuts import render, redirect
from .models import PerroDetector

def inicioPerro(request):
    listadoPerros = PerroDetector.objects.all()
    return render(request, "PerrosDetector/inicioPerro.html", {'perros': listadoPerros})

def nuevoPerro(request):
    return render(request, "PerrosDetector/nuevoPerro.html")

def guardarPerro(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        raza = request.POST["raza"]
        edad = request.POST["edad"]
        estado = request.POST["estado"]

        PerroDetector.objects.create(nombre=nombre, raza=raza, edad=edad, estado=estado)

        return redirect('indexPerro')
    return redirect('indexPerro')

def eliminarPerro(request, id):
    perroEliminar = PerroDetector.objects.get(id=id)
    perroEliminar.delete()
    return redirect('indexPerro')

def editarPerro(request, id):
    perro = PerroDetector.objects.get(id=id)
    return render(request, "PerrosDetector/editarPerro.html", {'perro': perro})

def procesarEdicionPerro(request, id):
    nombre = request.POST["nombre"]
    raza = request.POST["raza"]
    edad = request.POST["edad"]
    estado = request.POST["estado"]

    perro = PerroDetector.objects.get(id=id)
    perro.nombre = nombre
    perro.raza = raza
    perro.edad = edad
    perro.estado = estado
    perro.save()

    return redirect('indexPerro')

from django.shortcuts import render, redirect
from .models import Ventas
# Create your views here.

def inicio_vista(request):
    lasVentas=Ventas.objects.all

    return render(request,"gestionarMateria.html", {"misventas":lasVentas})

def registrarMateria(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtmateria"]
    creditos=request.POST["numcreditos"]
    guardarmateria=Ventas.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)
    return redirect("/")

def seleccionarMateria(request,codigo):
    materia=Ventas.objects.get(codigo=codigo)
    return render(request, "editarVentas.html", {"misventas": Ventas})

def editarMateria(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtmateria"]
    creditos=request.POST["numcreditos"]
    materia=Ventas.objects.get(codigo=codigo)
    materia.nombre=nombre
    materia.codigo=codigo
    materia.creditos=creditos
    materia.save()
    return redirect("/")

def borrarMateria(request, codigo):
    materia=Ventas.objects.get(codigo=codigo)
    materia.delete()

    return redirect("/")
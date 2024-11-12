from django.urls import path
from ventas_app import views

urlpatterns = [
    path("", views.inicio_vista, name="inicio_vista"),
    path("registrarMateria/", views.registrarMateria, name="registrarMateria"),
    path("seleccionarMateria/<codigo>", views.seleccionarMateria, name="selecionarMateria"),
    path("editarMateria/<codigo>", views.editarMateria, name="editarMateria"),
    path("borrarMateria/<codigo>", views.borrarMateria, name="borrarMateria")
    ]

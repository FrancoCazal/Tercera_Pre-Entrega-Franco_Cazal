from django.urls import path, include
from django.contrib import admin
from .views import *

urlpatterns = [
    path('', home, name="home"),

    # Doctores
    path('doctores/', doctores, name="doctores"),
    path('doc_create/', doctorCreate, name="doc_create"),

    # Funcionarios
    path('funcionarios/', funcionarios, name="funcionarios"),
    path('funcionario_create/', funcionarioCreate, name="funcionario_create"),


    # Clientes
    path('clientes/', clientes, name="clientes"),
    path('cliente_create/', clienteCreate, name="cliente_create"),

    # Mascotas
    path('mascotas/', mascotas, name="mascotas"),
    path('mascota_create/', mascotaCreate, name="mascota_create"),

    # Búsqueda
    path('buscar_datos/', buscarDatos, name="buscar_datos"),
    path('encontrar_datos/', encontrarDatos, name="encontrar_datos"),

    # Otros
    path('datos/', datos, name="datos"),
]

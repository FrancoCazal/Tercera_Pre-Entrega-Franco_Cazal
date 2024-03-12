from django.template import Template, Context
from django.http import HttpResponse

# Aquí se definen todas las funciones que resuelven las peticiones

def saludar(request):
    return HttpResponse("Bienvenidos a la Comision 50215 - Clase de Django")

def bienvenido(request, nombre, apellido):
    return HttpResponse(f"Bienvenido {nombre} {apellido}")
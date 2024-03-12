from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import *
from .forms import *

# Create your views here.

# Inicio
def home(request):
    return render(request, "aplicacion/home.html")

# Doctores
def doctores(request):
    contexto = {'doctores': Doctor.objects.all()}
    return render(request, "aplicacion/doctores.html", contexto)

def doctorCreate(request):
    if request.method == "POST":
        miForm = DoctorForm(request.POST)
        if miForm.is_valid():
            doctor_nombre = miForm.cleaned_data.get("nombre")
            doctor_apellido = miForm.cleaned_data.get("apellido")
            doctor_nro_registro = miForm.cleaned_data.get("nro_registro")
            doctor = Doctor(nombre=doctor_nombre,
                            apellido=doctor_apellido,
                            nro_registro=doctor_nro_registro)
            doctor.save()

            return redirect(reverse_lazy('doctores'))
    else:
        miForm = DoctorForm()
    return render(request, "aplicacion/doctorForm.html", {"form": miForm})
    

# Funcionarios
def funcionarios(request):
    contexto = {'funcionarios': Funcionario.objects.all()}
    return render(request, "aplicacion/funcionarios.html", contexto)

def funcionarioCreate(request):
    if request.method == "POST":
        miForm = FuncionarioForm(request.POST)
        if miForm.is_valid():
            funcionario_nombre = miForm.cleaned_data.get("nombre")
            funcionario_apellido = miForm.cleaned_data.get("apellido")
            funcionario_funcion = miForm.cleaned_data.get("funcion")
            funcionario_sueldo = miForm.cleaned_data.get("sueldo")
            funcionario = Funcionario(nombre=funcionario_nombre,
                                      apellido=funcionario_apellido,
                                      funcion=funcionario_funcion,
                                      sueldo=funcionario_sueldo)
            funcionario.save()

            return redirect(reverse_lazy('funcionarios'))
    else:
        miForm = FuncionarioForm()
    return render(request, "aplicacion/funcionarioForm.html", {"form": miForm})

# Clientes
def clientes(request):
    contexto = {'clientes': Cliente.objects.all()}
    return render(request, "aplicacion/clientes.html", contexto)

def clienteCreate(request):
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            cliente_nombre = miForm.cleaned_data.get("nombre")
            cliente_apellido = miForm.cleaned_data.get("apellido")
            cliente_nro_documento = miForm.cleaned_data.get("nro_documento")
            cliente = Cliente(nombre=cliente_nombre,
                              apellido=cliente_apellido,
                              nro_documento=cliente_nro_documento)
            cliente.save()

            return redirect(reverse_lazy('clientes'))
    else:
        miForm = ClienteForm()
    return render(request, "aplicacion/clienteForm.html", {"form": miForm})

# Mascotas
def mascotas(request):
    contexto = {'mascotas': Mascota.objects.all()}
    return render(request, "aplicacion/mascotas.html", contexto)

def mascotaCreate(request):
    if request.method == "POST":
        miForm = MascotaForm(request.POST)
        if miForm.is_valid():
            mascota_nombre = miForm.cleaned_data.get("nombre")
            mascota_edad = miForm.cleaned_data.get("edad")
            mascota_especie = miForm.cleaned_data.get("especie")
            mascota_raza = miForm.cleaned_data.get("raza")
            mascota = Mascota(nombre=mascota_nombre,
                              edad = mascota_edad,
                              especie=mascota_especie,
                              raza=mascota_raza)
            mascota.save()

            return redirect(reverse_lazy('mascotas'))
    else:
        miForm = MascotaForm()
    return render(request, "aplicacion/mascotaForm.html", {"form": miForm})

# Búsqueda
def buscarDatos(request):
    return render(request, "aplicacion/buscar.html")

def encontrarDatos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        doctores = Doctor.objects.filter(nombre__icontains=patron)
        funcionarios = Funcionario.objects.filter(nombre__icontains=patron)
        clientes = Cliente.objects.filter(nombre__icontains=patron)
        mascotas = Mascota.objects.filter(nombre__icontains=patron)
        contexto = {"doctores": doctores, "funcionarios": funcionarios, "clientes": clientes, "mascotas": mascotas}
        return render(request, "aplicacion/datos.html", contexto)
    
    contexto = {'doctores':Doctor.objects.all(),'funcionarios':Funcionario.objects.all(), 'clientes':Cliente.objects.all(), 'mascotas':Mascota.objects.all()}
    return render(request, "aplicacion/pagina.html", contexto)

# Otros
def datos(request):
    contexto = {'doctores':Doctor.objects.all(),'funcionarios':Funcionario.objects.all(), 'clientes':Cliente.objects.all(), 'mascotas':Mascota.objects.all()}
    return render(request, "aplicacion/datos.html", contexto)
from django import forms

class DoctorForm(forms.Form):
    nombre = forms.CharField(max_length=40, required=True)
    apellido = forms.CharField(max_length=40, required=True)
    nro_registro = forms.IntegerField()

class FuncionarioForm(forms.Form):
    nombre = forms.CharField(max_length=40, required=True)
    apellido = forms.CharField(max_length=40, required=True)
    funcion = forms.CharField(max_length=40, required=True)
    sueldo = forms.IntegerField()

class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=40, required=True)
    apellido = forms.CharField(max_length=40, required=True)
    nro_documento = forms.IntegerField()

class MascotaForm(forms.Form):
    nombre = forms.CharField(max_length=40, required=True)
    edad = forms.IntegerField()
    especie = forms.CharField(max_length=40, required=True)
    raza = forms.CharField(max_length=40, required=True)
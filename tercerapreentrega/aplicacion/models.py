from django.db import models

# En este archivo se crean los modelos

# Doctor, Funcionario, Cliente, Mascota

class Doctor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    nro_registro = models.IntegerField()

    class Meta:
        ordering = ["nombre", "apellido"]
        verbose_name = "Doctor"
        verbose_name_plural = "Doctores"

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Funcionario(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    funcion = models.CharField(max_length=20)
    sueldo = models.IntegerField()

    class Meta:
        ordering = ["nombre", "apellido"]

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    nro_documento = models.IntegerField()

    class Meta:
        ordering = ["nombre", "apellido"]

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Mascota(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    especie = models.CharField(max_length=40)
    raza = models.CharField(max_length=40)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.nombre}, {self.especie}, {self.raza}"
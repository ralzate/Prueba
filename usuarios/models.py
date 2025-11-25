from django.db import models

class Medico(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    genero = models.CharField(max_length=10)
    telefono = models.CharField(max_length=15)
    tipo_documento = models.CharField(max_length=50)
    numero_documento = models.CharField(max_length=50, unique=True)
    especialidad = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    genero = models.CharField(max_length=10)
    telefono = models.CharField(max_length=15)
    tipo_documento = models.CharField(max_length=50)
    numero_documento = models.CharField(max_length=50, unique=True)
    ocupacion = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.nombre} - {self.especialidad}"
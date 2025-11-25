from django.db import models

class Especialidad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    
class Cie10(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    descripcion = models.TextField()
    extra_v     = models.TextField()
    sub_grupo   = models.IntegerField()
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.codigo} - {self.descripcion}"
from django.db import models
from usuarios.models import Paciente
from usuarios.models import Medico
from referencias.models import Cie10

class Consulta(models.Model):
    paciente_id = models.fieldName = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico_id = models.fieldName = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    motivo_consulta = models.TextField()
    analisis_medico = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Consulta de {self.paciente} el {self.fecha.strftime('%Y-%m-%d %H:%M')}"

class Diagnostico(models.Model):
    consulta_id = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    cie10_id = models.ForeignKey(Cie10, on_delete=models.CASCADE)
    descripcion = models.TextField()
    tratamiento = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Diagnostico para consulta {self.consulta.id}"
    

class RegistroSignosVitales(models.Model):
    consulta_id = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    presion_arterial = models.CharField(max_length=20)
    frecuencia_cardiaca = models.IntegerField()
    frecuencia_respiratoria = models.IntegerField()
    temperatura = models.FloatField()
    saturacion_oxigeno = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Signos Vitales para consulta {self.consulta.id}"


# class HistoriaClinica(models.Model):
  #  paciente_id = models.ForeignKey(Paciente, on_delete=models.CASCADE)
   # consultas = models.ManyToManyField(Consulta)
   # diagnosticos = models.ManyToManyField(Diagnostico)
   # created_at = models.DateTimeField(auto_now_add=True)
   # updated_at = models.DateTimeField(auto_now=True)

   # def __str__(self):
   #     return f"Historia Clinica de {self.paciente}"
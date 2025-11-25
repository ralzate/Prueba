from django import forms
from .models import Consulta, Diagnostico, RegistroSignosVitales

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['paciente_id', 'medico_id', 'motivo_consulta', 'analisis_medico']

class DiagnosticoForm(forms.ModelForm):
    class Meta:
        model = Diagnostico
        fields = ['consulta_id', 'cie10_id', 'descripcion', 'tratamiento']

class RegistroSignosVitalesForm(forms.ModelForm):
    class Meta:
        model = RegistroSignosVitales
        fields = ['consulta_id', 'presion_arterial', 'frecuencia_cardiaca', 'frecuencia_respiratoria', 'temperatura', 'saturacion_oxigeno']
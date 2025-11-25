from django import forms
from .models import Especialidad, Cie10

class EspecialidadForm(forms.ModelForm):
    class Meta:
        model = Especialidad
        fields = ['nombre', 'descripcion']

class Cie10Form(forms.ModelForm):
    class Meta:
        model = Cie10
        fields = ['codigo', 'descripcion', 'extra_v', 'sub_grupo']
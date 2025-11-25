from django.shortcuts import render, redirect
from django.views import View
from .models import Especialidad, Cie10
from .forms import EspecialidadForm, Cie10Form


def especialidades(request):
    especialidades = Especialidad.objects.all()
    return render(request, 'especialidades.html', {'especialidades': especialidades})

def crear_especialidad(request):
    if request.method == 'POST':
        form = EspecialidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('especialidades')
    else:
        form = EspecialidadForm()

    return render(request, 'crear_especialidad.html', {'form': form})


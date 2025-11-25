from django.shortcuts import render
from django.views import View
from .models import Consulta

class ConsultaListCreateView(View):
    def get(self, request):
        consultas = Consulta.objects.all()
        return render(request, 'historia_clinica/consulta.html', {'consultas': consultas})


from django.shortcuts import render
from django.views import View
# from mysqlx import View
from .models import Consulta

class ConsultaListCreateView(View):
    def get(self, request):
        consultas = Consulta.objects.all()
        return render(request, 'historia_clinica/consulta.html', {'consultas': consultas})
    
    def post(self, request):
        paciente_id = request.POST.get('paciente_id')
        medico_id = request.POST.get('medico_id')
        motivo_consulta = request.POST.get('motivo_consulta')
        analisis_medico = request.POST.get('analisis_medico')

        consulta = Consulta.objects.create(
            paciente_id=paciente_id,
            medico_id=medico_id,
            motivo_consulta=motivo_consulta,
            analisis_medico=analisis_medico
        )
        return render(request, 'historia_clinica/crear_consulta.html', {'consulta': consulta})


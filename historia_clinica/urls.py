from django.urls import path
from . import views

urlpatterns = [
    path('consultas/', views.ConsultaListCreateView.as_view(), name='consultas'),
    path('crear_consulta/', views.ConsultaListCreateView.as_view(), name='crear_consulta'),
]
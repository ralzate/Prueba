from django.urls import path
from . import views

urlpatterns = [
    path('especialidades/', views.especialidades, name='especialidades'),
    path('crear_especialidad/', views.crear_especialidad, name='crear_especialidad'),
]
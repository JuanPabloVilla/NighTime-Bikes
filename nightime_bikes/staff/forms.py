from django import forms
from .models import Empleado, Horario


class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ['nombre_h', 'tiempo_inicial', 'tiempo_final']
        labels = {
            'nombre_h': 'Nombre del horario',
            'tiempo_inicial': 'Hora de entrada',
            'tiempo_final': 'Hora de salida',
        }
        widgets = {
            'tiempo_inicial': forms.TimeInput(attrs={'type': 'time'}),
            'tiempo_final': forms.TimeInput(attrs={'type': 'time'}),
        }


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['usuario', 'cedula', 'telefono', 'direccion', 'estado', 'horario']
        labels = {
            'usuario': 'Usuario del empleado',
            'cedula': 'Cedula',
            'telefono': 'Telefono',
            'direccion': 'Direccion',
            'estado': 'Estado (activo, descanso o deshabilitado)',
            'horario': 'Horario asignado',
        }

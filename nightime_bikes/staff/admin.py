from django.contrib import admin
from .models import Empleado, Horario


# Register your models here.
@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ('nombre_h', 'tiempo_inicial', 'tiempo_final')
    search_fields = ('nombre_h',)


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'cedula', 'telefono', 'estado', 'horario')
    list_filter = ('estado', 'horario')
    search_fields = ('usuario', 'cedula')
    list_editable = ('estado', 'horario')
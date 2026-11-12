from django.contrib import admin
from .models import perfil


@admin.register(perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'rol', 'cedula', 'estado')
    list_filter = ('rol', 'estado')

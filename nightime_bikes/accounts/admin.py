from django.contrib import admin
from .models import perfil


# Register your models here.
@admin.register(perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'rol', 'cedula', 'estado')
    list_filter = ('rol', 'estado')
    search_fields = ('usuario__username', 'cedula')

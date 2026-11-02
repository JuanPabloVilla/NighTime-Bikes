from django.shortcuts import render
from . import models

# Create your views here.
def conexion_accounts(request):
    return render(request, models.perfil, name='perfiles')
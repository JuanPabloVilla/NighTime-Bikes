from django.shortcuts import render
#Importar la informacion del models
from .models import *

# Create your views here.

#Views para mostrar los productos en el templates
def mostrar_productos(request):
    productos_disponibles = productos.objects.filter(estado=True)
    categorias_disponibles = categorias.objects.all()
    lista_productos = {
        'productos': productos_disponibles,
        'categorias': categorias_disponibles,
    }
    return render(request, 'catalog/productos.html', lista_productos)

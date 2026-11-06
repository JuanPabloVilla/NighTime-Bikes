from django.shortcuts import render
#Importar la informacion del models
from .models import productos, categorias

# Create your views here.

#Views para mostrar los productos en el templates
def mostrar_productos(request):
    productos_disponibles = productos.objects.filter(estado=True)
    categorias_disponibles = categorias.objects.all()
    contexto = {
        'productos': productos_disponibles,
        'categorias': categorias_disponibles,
    }
    return render(request, 'catalog/index.html', contexto)

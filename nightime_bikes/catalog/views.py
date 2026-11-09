from django.shortcuts import render
#Importar la informacion del models
from .models import productos, categorias

# Create your views here.

#Views para mostrar los productos en el templates index
def mostrar_productos(request):
    # Buscamos productos de cada categoría y cortamos la lista con [:3]
    bicis = productos.objects.filter(estado=True, categoria__nombre_categoria__iexact='Bicicletas')[:3]
    accesorios = productos.objects.filter(estado=True, categoria__nombre_categoria__iexact='Accesorios')[:3]
    indumentaria = productos.objects.filter(estado=True, categoria__nombre_categoria__iexact='Indumentaria')[:3]
    
    contexto = {
        'bicis': bicis,
        'accesorios': accesorios,
        'indumentaria': indumentaria,
    }
    return render(request, 'catalog/index.html', contexto)

#Views para mostrar los productos en el templates filtro bicicletas
def mostrar_bicis(request):
    lista_bicis = productos.objects.filter(estado=True, categoria__nombre_categoria__iexact='Bicicletas')
    contexto = {
        'productos': lista_bicis,
    }
    return render(request, 'catalog/index.html', contexto)

#Views para mostrar los productos en el templates lista accesorios
def mostrar_accesorios(request):
    lista_accesorios = productos.objects.filter(estado=True, categoria__nombre_categoria__iexact='Accesorios')
    contexto = {
        'productos': lista_accesorios,
    }
    return render(request, 'catalog/accesorios.html', contexto)

#Views para mostrar los productos en el templates filtro indumentaria
def mostrar_indumentaria(request):
    lista_indumentaria = productos.objects.filter(estado=True, categoria__nombre_categoria__iexact='Indumentaria')
    contexto = {
        'productos': lista_indumentaria,
    }
    return render(request, 'catalog/indumentaria.html', contexto)

from django.shortcuts import render
#Importar la informacion del models
from .models import productos

# Create your views here.

#Views para mostrar los productos en el templates index
def mostrar_productos(request):
    # Para obtener tres productos de cada categoria
    bicis = productos.objects.filter(estado=True, categoria__nombre_categoria__iexact='Bicicletas')[:3]
    accesorios = productos.objects.filter(estado=True, categoria__nombre_categoria__iexact='Accesorios')[:3]
    indumentaria = productos.objects.filter(estado=True, categoria__nombre_categoria__iexact='Indumentaria')[:3]

    # Para cargar los datos de los models que guardamos antes
    contexto = {
        'bicis': bicis,
        'accesorios': accesorios,
        'indumentaria': indumentaria,
    }
    return render(request, 'catalog/index.html', contexto)

#Views para mostrar los productos en el templates filtro bicicletas
def mostrar_bicis(request):
    lista_bicis = productos.objects.filter(estado=True, categoria__nombre_categoria__iexact='Bicicletas')

    # Para que el buscador funcione
    buscar = request.GET.get('buscar')
    ordenar = request.GET.get('ordenar')
    
    if buscar:
        lista_bicis = lista_bicis.filter(nombre_p__icontains=buscar)
    if ordenar == 'precio_asc':
        lista_bicis = lista_bicis.order_by('precio')
    elif ordenar == 'precio_desc':
        lista_bicis = lista_bicis.order_by('-precio')

    # Para usar la informacion
    contexto = {
        'productos': lista_bicis,
        'buscar': buscar,
        'ordenar': ordenar,
    }

    return render(request, 'catalog/bicicletas.html', contexto)

#Views para mostrar los productos en el templates lista accesorios
def mostrar_accesorios(request):
    lista_accesorios = productos.objects.filter(estado=True, categoria__nombre_categoria__iexact='Accesorios')

    # Para que el buscador funcione
    buscar = request.GET.get('buscar')
    ordenar = request.GET.get('ordenar')
    
    if buscar:
        lista_accesorios = lista_accesorios.filter(nombre_p__icontains=buscar)
    if ordenar == 'precio_asc':
        lista_accesorios = lista_accesorios.order_by('precio')
    elif ordenar == 'precio_desc':
        lista_accesorios = lista_accesorios.order_by('-precio')

    # Para usar la informacion
    contexto = {
        'productos': lista_accesorios,
        'buscar': buscar,
        'ordenar': ordenar,
    }

    return render(request, 'catalog/accesorios.html', contexto)

#Views para mostrar los productos en el templates filtro indumentaria
def mostrar_indumentaria(request):
    lista_indumentaria = productos.objects.filter(estado=True, categoria__nombre_categoria__iexact='Indumentaria')

    # Para que el buscador funcione
    buscar = request.GET.get('buscar')
    ordenar = request.GET.get('ordenar')
    
    if buscar:
        lista_indumentaria = lista_indumentaria.filter(nombre_p__icontains=buscar)
    if ordenar == 'precio_asc':
        lista_indumentaria = lista_indumentaria.order_by('precio')
    elif ordenar == 'precio_desc':
        lista_indumentaria = lista_indumentaria.order_by('-precio')

    # Para usar la informacion
    contexto = {
        'productos': lista_indumentaria,
        'buscar': buscar,
        'ordenar': ordenar,
    }

    return render(request, 'catalog/indumentaria.html', contexto)
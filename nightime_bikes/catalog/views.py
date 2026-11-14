from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
#Importar la informacion del models
from .forms import ProductoForm
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
    return render(request, 'catalog/bicis.html', contexto)

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



# _________________________________________________
# Parte para crear y editar productos (administracion)
# _________________________________________________

def lista_productos(request):
    query = request.GET.get('q', '').strip()
    queryset = productos.objects.all().order_by('-id')
    if query:
        queryset = queryset.filter(
            Q(nombre_p__icontains=query) | Q(categoria__nombre_categoria__icontains=query)
        )
    paginator = Paginator(queryset, 5)
    page_obj = paginator.get_page(request.GET.get('page'))
    contexto = {
        'page_obj': page_obj,
        'query': query,
        'total_registros': paginator.count,
    }
    return render(request, 'catalog/lista_productos.html', contexto)


def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'catalog/form_producto.html',
                  {'form': form, 'titulo': 'Registrar nuevo producto'})


def editar_producto(request, pk):
    producto = get_object_or_404(productos, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'catalog/form_producto.html',
                  {'form': form, 'titulo': f'Editar producto: {producto.nombre_p}'})

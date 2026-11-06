from django.shortcuts import render, get_object_or_404, redirect
#Biblioteca para requerir el login
from django.contrib.auth.decorators import login_required
#Importacion de la informacion de los modelos del carrito
from .models import Carrito, items_carrito
#Importacion de los modelos de la app catalog
from catalog.models import productos

# Create your views here.

#Para exigir el login del usuario
@login_required(login_url='accounts/login')

#Funcion para agregar los productos al carrito
def agregarAl_carrito(request, producto_id):
    if request.method == 'POST':
        
        #Para traer el objeto seleccionado por el id
        producto_seleccionado = get_object_or_404(productos, id=producto_id)
        
        #Para crear el carrito del usuario o crearlo si no tiene 
        carrito, created = Carrito.objects.get_or_create(usuario=request.user.perfil)
        
        #Condicional para verificar si el producto estaba o no en el carrito 
        item, item_created = items_carrito.objects.get_or_create(
            carrito=carrito,
            producto=producto_seleccionado,
            defaults={'precio_unitario': producto_seleccionado.precio, 'cantidad': 1}
        )
        if not item_created:
            item.cantidad += 1
            item.save()

    #Para llevar al usuario a la pagina del carrito
    return redirect('ver_carrito')

#Funcion para mostrar, editar o eliminar los productos en el template
def ver_carrito(request):
    
    #Para obtener el carrito del usuario
    carrito, created = Carrito.objects.get_or_create(usuario=request.user.perfil, estado_pedido=True)

    #Para traer los items que estan en el carrito
    items = carrito.items.all()

    #El precio total del producto seleccionado
    total = sum(item.cantidad * item.precio_unitario for item in items)

    #Para guardar el total para la factura
    carrito.total_pagar = total
    carrito.save()

    #Para devolver los items y el total
    return render(request, 'cart/carrito.html', {'items': items,'total': total})

#Funciones para ajustar cantidad de productos o eliminar el producto del carrito

#Para el boton de aumentar y disminuir
def actualizar_cantidad(request, item_id, accion):

    #Obtener el producto por id
    item = get_object_or_404(items_carrito, id=item_id)

    #Condicional para definir la accion del boton y si aumenta o disminuye
    if accion == 'sumar':
        item.cantidad += 1
    elif accion == 'restar' and item.cantidad > 1:
        item.cantidad -= 1
    item.save()

    #Lleva nuevamente al carrito
    return redirect(request, 'ver_carrito')

#Para el boton de eliminar
def eliminar_item(request, item_id):

    #obtener producto por id
    item = get_object_or_404(items_carrito, id=item_id)

    #Para eliminar el producto seleccionado
    item.delete()

    #volvemos al carrito
    return redirect('Carrito')

#Funcion para generar la factura
def generar_factura(request):
    #Para obtener la informacion del carrito activo por usuario
    carrito = Carrito.objects.filter(usuario=request.user.perfil, estado_pedido=True).first()

    #Para obtener los items del carrito
    items = carrito.items.all()

    #Condicional para cerrar el carrito
    if items.exists():
        carrito.estado_pedido = False
        carrito.save()

        #lo enviamos a una lista con todas las compras completadas (facturas)
        return redirect('ver_factura', carrito_id=carrito.id)
    return redirect('ver_carrito')
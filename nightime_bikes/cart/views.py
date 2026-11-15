from django.shortcuts import render, get_object_or_404, redirect
#Biblioteca para requerir el login
from django.contrib.auth.decorators import login_required
#Importacion de la informacion de los modelos del carrito
from .models import Carrito, items_carrito
#Importacion de los modelos de la app catalog
from catalog.models import productos
# Importacion de la cuenta
from accounts.models import perfil 
# para generar mensajes
from django.contrib import messages
# Create your views here.
# _________________________________________________
# Parte para las views del carrito
# _________________________________________________

# Funcion para buscar el perfil del usuario
def obtener_perfil(usuario):
    perfil_obj, created = perfil.objects.get_or_create(usuario=usuario)
    return perfil_obj

def agregarAl_carrito(request, producto_id):
    # Mensaje por si el usuario no esta registrado/logeado y entra al carrito
    if not request.user.is_authenticated:
        messages.warning(request, "Debes iniciar sesión para añadir productos a tu carrito.")
        return redirect('login')
    #Funcion para agregar los productos al carrito
    if request.method == 'POST':
        
        #Para traer el objeto seleccionado por el id
        producto_seleccionado = get_object_or_404(productos, id=producto_id)

        # para obtener el perfil del usuario
        perfil_usuario = obtener_perfil(request.user)

        #Para crear el carrito del usuario o crearlo si no tiene 
        carrito, created = Carrito.objects.get_or_create(usuario=perfil_usuario, estado_pedido=True)
        
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
    # Mensaje por si el usuario no esta registrado/logeado y entra al carrito
    if not request.user.is_authenticated:
        messages.warning(request, "Debes iniciar sesión para poder ver y gestionar tu carrito.")
        return redirect('login')
    # para obtener el perfil del usuario
    perfil_usuario = obtener_perfil(request.user)

    #Para obtener el carrito del usuario
    carrito, created = Carrito.objects.get_or_create(usuario=perfil_usuario, estado_pedido=True)

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
@login_required(login_url='login')
def actualizar_cantidad(request, item_id, accion):

    #Obtener el producto por id
    item = get_object_or_404(items_carrito, id=item_id)

    #Condicional para definir la accion del boton y si aumenta o disminuye
    if accion == 'sumar':
        if item.cantidad >= item.producto.stock:
            messages.error(request, f'Lo sentimos, no hay más stock disponible de {item.producto.nombre_p}.')
        else:
            item.cantidad += 1
            item.save()
    elif accion == 'restar' and item.cantidad > 1:
        item.cantidad -= 1
        item.save()

    #Lleva nuevamente al carrito
    return redirect('ver_carrito')

#Para el boton de eliminar
@login_required(login_url='login')
def eliminar_item(request, item_id):

    #obtener producto por id
    item = get_object_or_404(items_carrito, id=item_id)

    #Para eliminar el producto seleccionado
    item.delete()

    #volvemos al carrito
    return redirect('ver_carrito')


# _________________________________________________
# Parte para las views de las facturas
# _________________________________________________

#Funcion para generar la factura
@login_required(login_url='login')
def generar_factura(request):

    # para obtener el perfil del usuario
    perfil_usuario = obtener_perfil(request.user)

    #Para obtener la informacion del carrito activo por usuario, cerrarlo y pasar la informacion a factura
    carrito = Carrito.objects.filter(usuario=perfil_usuario, estado_pedido=True).first()

    #Para obtener los items del carrito
    if carrito:
        items = carrito.items.all()

        #Condicional para cerrar el carrito
        if items.exists():
            for item in items:
                producto = item.producto
                # para quitar cantidad del inventario
                producto.stock -= item.cantidad
                # para evitar que el stock quede en negativo
                if producto.stock < 0:
                    producto.stock = 0
                # para marcar como no disponible en la gestion
                if producto.stock == 0:
                    producto.estado = False
                producto.save()
            # Para cerrar el carrito y permitir la facturacion
            carrito.estado_pedido = False
            carrito.save()

            #lo enviamos a una lista con todas las compras completadas (facturas)
            return redirect('ver_factura', carrito_id=carrito.id)
    return redirect('ver_carrito')

def ver_factura(request, carrito_id):
    # Mensaje por si el usuario no esta registrado/logeado y entrar a la factura
    if not request.user.is_authenticated:
        messages.warning(request, "Debes iniciar sesión para poder ver los detalles de tu factura.")
        return redirect('login')
    # para obtener el perfil del usuario
    perfil_usuario = obtener_perfil(request.user)

    #Para buscar el carrito cerrado y la informacion que contenia
    factura = get_object_or_404(Carrito, id=carrito_id, usuario=perfil_usuario, estado_pedido=False)
    items = factura.items.all()
    # Para sacar el subtotal de cada producto segun la cantidad
    for item in items:
        item.subtotal = item.cantidad * item.precio_unitario
    
    return render(request, 'cart/factura.html', {'factura': factura, 'items': items}, )

def historial_facturas(request):
    # Mensaje por si el usuario no esta registrado/logeado y entrar a la factura
    if not request.user.is_authenticated:
        messages.warning(request, "Debes iniciar sesión para poder ver los detalles de tu factura.")
        return redirect('login')
    # para obtener el perfil del usuario
    perfil_usuario = obtener_perfil(request.user)
    # Para generar la factura segun el usuario ordenado por la fecha de creacion
    facturas = Carrito.objects.filter(usuario=perfil_usuario, estado_pedido=False).order_by('-fecha_pedido')
    return render(request, 'cart/historial.html', {'facturas':facturas})
from django.urls import path
from . import views

urlpatterns = [
    #Para ver el carrito
    path('ver/', views.ver_carrito, name='ver_carrito'),
    #Para agregar items al carrito (boton)
    path('agregar/<int:producto_id>/', views.agregarAl_carrito, name='agregar_al_carrito'),
    #Para aumentar o disminuir cantidad desde el carrito
    path('actualizar/<int:item_id>/<str:accion>/', views.actualizar_cantidad, name='actualizar_cantidad'),
    #Para eliminar productos del carrito
    path('eliminar/<int:item_id>/', views.eliminar_item, name='eliminar_item'),
    #La generacion de factura
    path('factura/', views.generar_factura, name='generar_factura'),
]
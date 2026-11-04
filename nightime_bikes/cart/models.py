from django.db import models

# Create your models here.
#Informacion basica de del usuario y el pedido para la factura
class pedido(models.Model):
    usuario = models.ForeignKey('accounts.perfil', on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    total_pagar = models.DecimalField(max_digits=10, decimal_places=2)
    estado_pedido = models.BooleanField(default=True)

#Informacion de los productos para la factura
class detalles_pedido(models.Model):
    pedido = models.ForeignKey(pedido, on_delete=models.CASCADE)
    productos = models.ForeignKey('catalog.productos', on_delete = models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

def __str__(self):
    return f"{self.cantidad}*{self.producto.nombre} (pedido #{self.pedido.id})"

def __str__(self):
    return self.cantidad *self.precio_unitario

#*pedidos (esta seria la informacion de la factura)
#-id_usuario
#-fecha_pedido
#-total_pagado
#-estado_pedido (pendiente, pagado, enviado)

#*detalles_pedido (los productos que contiene la factura)
#-id_pedido (a que factura estan relacionados los productos)
#-id_productos (que productos compro)
#-cantidad
#-precio_unitario
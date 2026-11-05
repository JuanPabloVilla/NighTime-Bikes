from django.db import models

# Create your models here.
#Informacion basica de del usuario y el pedido para la factura
class Carrito(models.Model):
    usuario = models.ForeignKey('accounts.perfil', on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    total_pagar = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00)
    estado_pedido = models.BooleanField(default=True)

    def __str__(self):
        return f"Carrito de {self.usuario.usuario.username}"

#Informacion de los productos para la factura
class items_carrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey('catalog.productos', on_delete = models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

def __str__(self):
    return f"{self.cantidad}*{self.producto.nombre} (pedido #{self.pedido.id})"
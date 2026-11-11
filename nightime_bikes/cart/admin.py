from django.contrib import admin
from .models import Carrito, items_carrito

# Esto permite ver los productos comprados dentro del Carrito (Factura)
class ItemCarritoInline(admin.TabularInline):
    model = items_carrito
    extra = 0 # No permitir añadir items manualmente desde el admin
    readonly_fields = ('producto', 'cantidad', 'precio_unitario')

@admin.register(Carrito)
class CarritoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'fecha_pedido', 'total_pagar', 'estado_pedido')
    list_filter = ('estado_pedido', 'fecha_pedido')
    search_fields = ('usuario__usuario__username',) # Busca por el nombre del usuario
    inlines = [ItemCarritoInline]

@admin.register(items_carrito)
class ItemCarritoAdmin(admin.ModelAdmin):
    list_display = ('id', 'carrito', 'producto', 'cantidad', 'precio_unitario')
    search_fields = ('producto__nombre_p',)
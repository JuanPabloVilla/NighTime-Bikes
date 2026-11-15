from django.contrib import admin
from .models import Carrito, items_carrito

# Para permitir ver los productos comprados dentro del Carrito (Factura)
class ItemCarritoInline(admin.TabularInline):
    model = items_carrito
    # para evitar añadir items manualmente desde el admin
    extra = 0 
    readonly_fields = ('producto', 'cantidad', 'precio_unitario')

@admin.register(Carrito)
class CarritoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'fecha_pedido', 'total_pagar', 'estado_pedido')
    list_filter = ('estado_pedido', 'fecha_pedido')
    # Para Buscar por el nombre del usuario
    search_fields = ('usuario__usuario__username',) 
    inlines = [ItemCarritoInline]

@admin.register(items_carrito)
class ItemCarritoAdmin(admin.ModelAdmin):
    list_display = ('id', 'carrito', 'producto', 'cantidad', 'precio_unitario')
    search_fields = ('producto__nombre_p',)
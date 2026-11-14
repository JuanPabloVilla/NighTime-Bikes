from django.contrib import admin
from .models import categorias, productos


# Register your models here.
@admin.register(categorias)
class CategoriasAdmin(admin.ModelAdmin):
    list_display = ('nombre_categoria', 'descripcion_c')
    search_fields = ('nombre_categoria',)


@admin.register(productos)
class ProductosAdmin(admin.ModelAdmin):
    list_display = ('nombre_p', 'categoria', 'precio', 'stock', 'estado')
    list_filter = ('categoria', 'estado')
    search_fields = ('nombre_p', 'descripcion_p')
    list_editable = ('precio', 'stock', 'estado')
from django.contrib import admin
from .models import categorias, productos
<<<<<<< HEAD

=======


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

>>>>>>> main
# Esto permite añadir productos directamente desde la vista de la Categoría
class ProductoInline(admin.TabularInline):
    model = productos
    extra = 1

@admin.register(categorias)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre_categoria', 'descripcion_c')
    search_fields = ('nombre_categoria',)
    inlines = [ProductoInline] # Muestra los productos dentro de la categoría

@admin.register(productos)
class ProductoAdmin(admin.ModelAdmin):
    # Columnas que se verán en la lista
    list_display = ('nombre_p', 'precio', 'stock', 'estado', 'categoria')
    # Filtros laterales (muy útiles para encontrar rápido)
    list_filter = ('estado', 'categoria')
    # Buscador
    search_fields = ('nombre_p', 'descripcion_p')
    # Para que el campo de la imagen se vea bien
<<<<<<< HEAD
    readonly_fields = ('id',)
=======
    readonly_fields = ('id',)
>>>>>>> main

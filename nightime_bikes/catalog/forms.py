from django import forms
from .models import productos


class ProductoForm(forms.ModelForm):
    class Meta:
        model = productos
        fields = ['nombre_p', 'descripcion_p', 'precio', 'imagen', 'categoria', 'stock', 'estado']
        labels = {
            'nombre_p': 'Nombre del producto',
            'descripcion_p': 'Descripcion',
            'precio': 'Precio',
            'imagen': 'Imagen',
            'categoria': 'Categoria',
            'stock': 'Stock disponible',
            'estado': 'Disponible',
        }
        widgets = {
            'descripcion_p': forms.Textarea(attrs={'rows': 4}),
        }
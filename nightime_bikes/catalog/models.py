from django.db import models

# Create your models here.

# Tabla de las categorias base de datos
class categorias(models.Model):
    nombre_categoria = models.CharField(max_length=50)
    descripcion_c = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.nombre_categoria

# Tabla de productos para la base de datos
class productos(models.Model):
    nombre_p = models.CharField(max_length=250)
    descripcion_p = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    # Varioble para el uso de imagenes
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    categoria = models.ForeignKey(categorias, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)
    estado = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre_p

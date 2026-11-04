from django.db import models

# Create your models here.

# Tabla de las categorias base de datos
class categorias(models.Model):
    nombre_categoria = models.CharField(50)
    descripcion_c = models.TextField(blank=True, null=True)

# Tabla de productos para la base de datos
class productos(models.Model):
    nombre_p = models.CharField(max_length=250)
    descripcion_p = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=4, decimal_places=2)
    # Varioble para el uso de imagenes
    imagen = models.ImageField(upload_to='productos/')
    categoria = models.ForeignKey(categorias, on_delete=models.CASCADE)
    stock = models.IntegerField()
    estado = models.BooleanField(default=True)

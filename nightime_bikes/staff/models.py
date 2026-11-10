from django.db import models

# Create your models here.
from django.db import models


# Tabla de horarios: guarda los turnos de trabajo de la tienda
# (por ejemplo Mañana, Tarde, Noche) con su hora de entrada y de salida.
class Horario(models.Model):
    nombre_h = models.CharField(max_length=50)
    tiempo_inicial = models.TimeField()
    tiempo_final = models.TimeField()

    def __str__(self):
        return f"{self.nombre_h} ({self.tiempo_inicial:%H:%M}, {self.tiempo_final:%H:%M})"


# Tabla de empleados: guarda los datos del personal de la tienda
# (usuario, cedula, telefono, direccion y estado). Cada empleado
# puede tener un horario asignado.
class Empleado(models.Model):
    usuario = models.CharField(max_length=50, unique=True)
    rol = models.CharField(max_length=20, default='empleado')
    cedula = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=20, default='activo')
    # llave foranea: cada empleado tiene un horario (como categoria en productos)
    horario = models.ForeignKey(Horario, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.usuario}, {self.cedula}"
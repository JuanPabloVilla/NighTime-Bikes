from django.db import models
from django.contrib.auth.models import User

#Tabla perfil para trabajar con los usuarios en la base de datos

class perfil(models.Model):
    ROLE_CHOICES = (
        ('cliente', 'Cliente'),
        ('empleado', 'Empleado'),
        ('admin', 'Administrador'),
    )
    
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    # Al crear cuenta no se puede seleccionar el rol, para empleados y admins el rolo debe ser otorgado
    rol = models.CharField(max_length=20, choices=ROLE_CHOICES, default='cliente') 
    cedula = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=20, default='Activo') 
    
    def __str__(self):
        return f"{self.usuario.username} - {self.rol}"
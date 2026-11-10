from django.urls import path
from . import views

urlpatterns = [
    # Para ver la lista de todos los empleados
    path('empleados/', views.lista_empleados, name='lista_empleados'),
    # Para ver el detalle de un empleado específico
    path('empleados/<int:pk>/', views.detalle_empleado, name='detalle_empleado'),
    # Para registrar un nuevo empleado
    path('empleados/crear/', views.crear_empleado, name='crear_empleado'),
    # Para editar la información de un empleado existente
    path('empleados/editar/<int:pk>/', views.editar_empleado, name='editar_empleado'),
    # Para ver la lista de horarios registrados
    path('horarios/', views.lista_horarios, name='lista_horarios'),
    # Para crear un nuevo horario
    path('horarios/crear/', views.crear_horario, name='crear_horario'),
    # Para modificar un horario existente
    path('horarios/editar/<int:pk>/', views.editar_horario, name='editar_horario'),
]
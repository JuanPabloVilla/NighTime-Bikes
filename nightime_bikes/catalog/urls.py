from django.urls import path
from . import views

urlpatterns = [
    path('', views.mostrar_productos, name='mostrar_productos'),
    path('bicis/', views.mostrar_bicis, name='mostrar_bicis'),
    path('accesorios/', views.mostrar_accesorios, name='mostrar_accesorios'),
    path('indumentaria/', views.mostrar_indumentaria, name='mostrar_indumentaria'),
    # ---- Parte para la gestion (admin): productos ----
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/crear/', views.crear_producto, name='crear_producto'),
    path('productos/editar/<int:pk>/', views.editar_producto, name='editar_producto'),
]
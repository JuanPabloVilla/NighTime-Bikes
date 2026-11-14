from django.urls import path
from . import views

urlpatterns = [
    # Pagina inicial, sera el index
    path('', views.mostrar_productos, name='mostrar_productos'),
    # Pagina para mostrar las bicis
    path('bicis/', views.mostrar_bicis, name='mostrar_bicis'),
    # Pagina para mostrar Accesorios
    path('accesorios/', views.mostrar_accesorios, name='mostrar_accesorios'),
    # Pagina para mostrar la indumentaria
    path('indumentaria/', views.mostrar_indumentaria, name='mostrar_indumentaria'),
    # ---- Parte para la gestion (admin): productos ----
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/crear/', views.crear_producto, name='crear_producto'),
    path('productos/editar/<int:pk>/', views.editar_producto, name='editar_producto'),
]
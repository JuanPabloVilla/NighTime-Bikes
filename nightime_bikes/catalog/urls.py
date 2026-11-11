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
]
from django.urls import path
from . import views

app_name = "Aplicacion"

urlpatterns = [
    path('post_listar', views.post_listar, name='post_listar'),
    path('acerca', views.acerca, name='acerca'),
    path('post_agregar', views.post_agregar, name='post_agregar'),
    path('post_buscar', views.post_buscar, name='post_buscar'),
    path('post_agregar_fabricante', views.post_agregar_fabricante, name='post_agregar_fabricante'),
    path('post_agregar_tipo', views.post_agregar_tipo, name='post_agregar_tipo'),
]
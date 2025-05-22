from django.urls import path
from . import views
#from django.contrib.auth import views as auth_views

app_name = "Aplicacion"

urlpatterns = [
    path('post_listar', views.post_listar, name='post_listar'),
    path('acerca', views.acerca, name='acerca'),
    path('post_buscar', views.post_buscar, name='post_buscar'),
    
    path('post_agregar', views.post_agregar, name='post_agregar'),

    path('post_agregar_fabricante', views.post_agregar_fabricante, name='post_agregar_fabricante'),
    path('post_eliminar_fabricante/<int:fabricante_id>/', views.post_eliminar_fabricante, name='post_eliminar_fabricante'),
    path('post_editar_fabricante/editar/<int:fabricante_id>/', views.post_editar_fabricante, name='post_editar_fabricante'),
    
    path('post_agregar_tipo', views.post_agregar_tipo, name='post_agregar_tipo'),
    path('post_eliminar_tipo/<int:tipo_id>/', views.post_eliminar_tipo, name='post_eliminar_tipo'),
    path('post_editar_tipo/<int:tipo_id>/', views.post_editar_tipo, name='post_editar_tipo'),    
]
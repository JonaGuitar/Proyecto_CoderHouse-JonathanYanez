# Poyecto_CoderHouse MVT

Consignas Finales para curso Python 


## Pasos para probar

1. Clonar el repositorio:
2. Crear entorno virtual y activarlo: (yo lo hice sin directorio virutal)
3. Instalar Django:
4. Migrar la base de datos:
5. Ejecutar el servidor:
6. Abrir en el navegador: http://127.0.0.1:8000/



## Estructura del Proyecto


**Aplicacion/**  
  Carpeta de la app principal que contiene las vistas, modelos y URLs.

  - **templates\Aplicacion**  
    Carpeta de la app principal que contiene los templates

    acercade.html
    agregar_fabricante.html
    agregar_tipo.html
    agregar_vehiculos.html
    buscar_vehiculos.html
    listar_vehiculos.html


**Main/**  
  Carpeta donde esta el layout del sitio y el accoubt de user.

  - **templates\Main/**  
    Carpeta de la app principal que contiene los templates

    index.html
    perfil.html
    editar_perfil.html
    registrar_usuario.html
    login.html
    logout.html
    password_change.html
    password_change_done.html




## Funcionalidades principales y sus URLs

-----------------------------------------------------------------------------------------------------
| Funcionalidad                    | Ubicación                      | URL accesible                 |
|----------------------------------|--------------------------------|-------------------------------|
| Página Acerca de                 | `Aplicacion/views.py`          | `/acerca`                     |
| Listar Publicaciones             | `Aplicacion/views.py`          | `/post_listar`                |
| Buscar Publicaciones             | `Aplicacion/views.py`          | `/post_buscar`                |
|                                  |                                |                               |
| Agregar Vehiculo                 | `Aplicacion/views.py`          | `/post_agregar`               |
| Actualizar Vehiculo              | `Aplicacion/views.py`          | `/post_editar_vehiculo`       |
| Eliminar Vehiculo                | `Aplicacion/views.py`          | `/post_eliminar_vehiculo`     |
|                                  |                                |                               |
| Agregar Fabricante               | `Aplicacion/views.py`          | `/post_agregar_fabricante`    |
| Actualizar Fabricante            | `Aplicacion/views.py`          | `/post_editar_fabricante`     |
| Eliminar Fabricante              | `Aplicacion/views.py`          | `/post_eliminar_fabricante`   |
|                                  |                                |                               |
| Agregar Tipo                     | `Aplicacion/views.py`          | `/post_agregar_tipo`          |
| Actualizar Tipo                  | `Aplicacion/views.py`          | `/post_editar_fabricante`     |
| Eliminar Tipo                    | `Aplicacion/views.py`          | `/post_eliminar_fabricante`   |          
|                                  |                                |                               |
| index                            | `Main/views.py`                | `/index`                      |
| perfil                           | `Main/views.py`                | `/perfil`                     |
| editar_perfil                    | `Main/views.py`                | `/editar_perfil`              |
| registrar_usuario                | `Main/views.py`                | `/registrar_usuario`          |                                                                
| login                            | `Main/views.py`                | `/login_usuario`              |  
| logout                           | `Main/views.py`                | `/logout_usuario`             |
-----------------------------------------------------------------------------------------------------



## LOGIN

  para el Login hay que tener creado un super usuario en django

  XXX
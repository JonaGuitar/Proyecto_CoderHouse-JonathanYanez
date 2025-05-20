# Poyecto_CoderHouse MVT

Consignas Finales para curso Python 

## Pasos para probar

1. Clonar el repositorio:
   ```bash
   git clone <repo_url>
   cd blog_project
   ```

2. Crear entorno virtual y activarlo:
   ```bash
   python -m venv env
   source env/bin/activate  # o env\Scripts\activate en Windows
   ```

3. Instalar Django:
   ```bash
   pip install django
   ```

4. Migrar la base de datos:
   ```bash
   python manage.py migrate
   ```

5. Ejecutar el servidor:
   ```bash
   python manage.py runserver
   ```

6. Abrir en el navegador: http://127.0.0.1:8000/

## Funcionalidades

- Crear autor: `/create-author/`
- Crear categoría: `/create-category/`
- Crear post: `/create-post/`
- Buscar posts por título: `/search/`
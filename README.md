<h1>Pasos para arrancar el proyecto.</h1> 

1 - Clonar el proyecto o descargar archivo comprimido.

2 - Instalar las dependencias del proyecto: 

        2.1 pip install -r requirements.txt.

3 - Crear las migraciones para generar la base de datos

    3.1 ejecutar el comando python manage.py makemigrations "nombredelaaplicacion"
    3.2 python manage.py sqlmigrate nombredelaaplicacion 0001
    3.3 python manage.py makemigrations y luego python manage.py migrate.

4 - Iniciar el servidor con el comando python manage.py runserver.

5 - Una vez arrancado el servidor, ingresar al siguiente link: http://localhost:8000/

6 - Registrarse para poder ingresar.

6.1 - Los datos pueden modificarse más adelante, y agregar una descripción y avatar.

7 - Registrar videojuegos.

7 - Editar Videojuegos

7.1 Se puede editar un videojuego pudiendo modificar sus atributos de texto como de imagen.

8 - Se puede visualizar el apartado de detalles del videojuego pudiendo ver su titulo, descripción y su imagen (si tiene).

9 - Se puede ver el catálogo con los videojuegos creados o buscar alguno ya creado.

10 - En el apartado Acerca de Nosotros podrás saber más sobre los integrantes del equipo.

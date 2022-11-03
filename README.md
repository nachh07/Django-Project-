<h1>Pasos para levantar el proyecto.</h1> 

1 - Clonar el proyecto o descargar archivo comprimido.

2 - Instalar las dependencias del proyecto: 

        2.1 pip install -r requirements.txt.

3 - Crear las migraciones para generar la base de datos

    3.1 ejecutar el comando python manage.py makemigrations "nombredelaaplicacion"
    3.2 python manage.py sqlmigrate nombredelaaplicacion 0001
    3.3 python manage.py makemigrations y luego python manage.py migrate.

4 - Iniciar el servidor con el comando python manage.py runserver.

5 - Una vez arrancado el servidor, ingresar al siguiente link: http://localhost:8000/

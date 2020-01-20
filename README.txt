CHALLENGE CODING OMNIBNK - DESARROLLADO POR: HEBERT LEONARDO ARDILA RIVERA

Requerimientos:
Docker
Django 
Django rest_framework
Python 3.6

Aplicacion desarrollada en python haciendo uso del rest framework de Django, se hace uso de una base de datos con Docker.

Pasos para ejecutar el programa:

1. Abrir una terminal e ir a la carpeta del proyecto dentro en Omnibank_1 y ejecutar el comando: docker-compose up --build prueba-db
2. Abrir otra terminal e ir a la carpeta del proyecto dentro en Omnibank_1 y ejecutar los siguientes comandos: 
	1. python manager.py makemigrations
	2. python manager.py migrate
	3. python manager.py runserver
3. Abrir un navegador y entre a la siguiente url: http://127.0.0.1:8000/accounts/login/
4. Crear un nuevo usuario para ingresar.
5. Al ingresar se vera una tabla vacia. Dar click en Create movie.
6. Al crear una nueva pelicula, esta tiene tres opciones, editar, eliminar, y ver detalles. Las peliculas agregadas se iran viendo en la tabla cada una con sus respectivas opciones.
7. Para cerrar sesion dar click en logout.

Requerimientos cumplidos:

1. The Application should include a RESTful API
2. A User should be able to SIGN UP to the APPLICATION
3. When a User SIGNS UP, it should create a new USER for the APPLICATION
4. A User should be able to LOG IN to the APPLICATION
5. A User should be able to LOG OUT to the APPLICATION
6. A User should be able to CREATE a new Movie in the Application
7. A User should be able to RETRIEVE a SINGLE Movie from the Application
8. A User should be able to RETRIEVE a LIST of Movies from the Application
9. A User should be able to UPDATE a Movie from the Application
10. A User should be able to DELETE a Movie in the Application


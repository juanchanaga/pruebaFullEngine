# Blog Django

Este es un proyecto de para prueba técnica usando el framework **Django**.



## Prerrequisitos para correr la aplicación

 - Instalar Django
 - Instalar MySqlServer o algún gestor de bases de datos de MySql
 - Descargar el repositorio de la aplicación
 - Configurar el archivo **"..\pruebaFullEngine\FullEngineProject\settings.py"** de la línea 78 a la 81 con los datos de la base de datos local
 - Crear una base de datos llamada **"pruebaFullEngine"**

## ¿Cómo correr la aplicación?

 - Abrir una terminal
 - Navegar hasta la carpeta del proyecto **"..\pruebaFullEngine"**
 - Correr el comando **python manage.py makemigrations**
 - Correr el comando **python manage.py migrate**
 - Correr el comando **".\venv\Scripts\activate"**
 - Correr el comando **python manage.py runserver**
 - Abrir un navegador en la ruta del localhost indicada en la terminal, normalmente **localhost:8000**
 - Probar la aplicación, para ello primero debe crea un usuario en el menú  **"Regitrarse"** de la barra de navegación para crear blogs
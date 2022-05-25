# Entregable_API_REST


1. Crear modelos.
2. Crear las vistas para consultar datos (get, post, put, delete):
 Dentro de diferentes clases, por ejemplo una para ver todo y otra para buscar por id
3. A su vez se crea el Serializer para validar los datos.
4. Crear las URLs en url.py llamando a las clases en las vistas creadas.

________________________________________________________________________________________

Ejecutar: "django-admin startproject aprendiendo_django

Comprobar si funciona, migrar el projecto: python manage.py migrate

Ejecutar server con: python manage.py runserver

______________________________________________________________
Dentro de settings.py tenemos diferentes apps en nuestro projecto, cada una hace una cosa diferente:
INSTALLED_APPS = [

    'django.contrib.admin',        ------> Panel de administracion
    
    'django.contrib.auth',         ------> Autenticacion
    
    'django.contrib.contenttypes',
    
    'django.contrib.sessions',
    
    'django.contrib.messages',
    
    'django.contrib.staticfiles',
    
]

Una app es un paquete en pyhon con una funcionalidad

____________________________________________________________________

Para generar nueva app: python manage.py startapp miApp
Aparecera una nueva carpeta en el proyecto con el nombre de la app y otros ficheros

_____________________________________________________________________

Las vistas se trabajan en views.py (dentro de cada app)

______________________________________________________________

Para las vistas, la idea es tener una layout y gracias a la sintaxis especial
que añade en html, puedo indicar los trozos de codigo html que van cambiando
en mi layout, dependiendo de la vista en la que me encuentre

____________________________________________________________________

Crear carpeta statics para meter css e imagenes y luego cargarla en el layout.html
con  href="{%static 'css/styles.css'%}
____________________________________________________________________ 

Recomendado usar virtual environment, mas info: https://docs.python.org/3/library/venv.html
Recomendado usar generador para .gitignore, más info: https://www.toptal.com/developers/gitignore

python -m venv nombreEntorno

Activar entorno, nombre de carpeta con el Script/activate

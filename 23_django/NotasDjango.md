
# Notas sobe Django
Django es un framework de desarrollo web de código abierto, escrito en Python, que respeta el patrón de diseño conocido como MVC (Modelo–Vista–Controlador). Fue desarrollado en origen para gestionar varias páginas orientadas a noticias de la World Company de Lawrence, Kansas, y fue liberada al público bajo una licencia BSD en julio de 2005; el framework fue nombrado en alusión al guitarrista de jazz gitano Django Reinhardt. En junio de 2008 fue anunciado que la recién formada Django Software Foundation se haría cargo de Django en el futuro.

## Instalación de Django.
Se recomienda tener un instalado el Python 3 (en lugar del 2.7).
Para instalar Django vamos a la página de [descarga] de Django y seguimos las instrucciones para la versión indicada (actual).
Para la instalación se utiliza pip. Por ejemplo, para instalar la versión 3.0.9 se utiliza el comando (en modo administrador):

_**pip install Django==3.0.9**_

Para ver que versión de Django tenemos instalada:

_**py -m django --version**_

## Creación de un proyecto en Django.
Para crear el proyecto de Django con el nombre _AprendiendoDjango_, navegamos hacia el directorio que nos interese y utilizamos el comando _django-admin_ con los siguientes parámetros:

_**django-admin starproject AprendiendoDjango**_

Dentro de la carpeta del proyecto se crea un directorio con el nombre del proyecto (en nuestro caso otra carpeta _Aprendiendo Django_), y el fichero _manage.py_ que es una utilidad escrita en python para manejar apps.
Una vez se ha creado el proyecto, es necesario hacer un "migrate" del proyecto. Para ello, nos dirigiremos a la carpeta del proyecto y ejecutaremos el comando:

_**py manage.py migrate**_

Esto nos crea el fichero de base de datos _db.sqlite3_ en el directorio _AprendiendoDjango_, dentro del proyecto.

## Arrancar el servidor de nuestro proyecto

Para arrancar el servidor incorporado en Django, utilizaremos la utilidad _manage.py_ escribiendo el comando:

_**py manage.py runserver**_

## Creación de una app en Django.

Una app es un paquete, programado en python, que añade una funcionalidad a servidor web. Podemos tener, por ejemplo, una app de entradas, otra de salidas, otra de consulta a bbdd, etc. 

Para crear la app llamada _miapp_, utilizaremos el fichero la utilidad _manage.py_ escribiendo el comando:

_**py manage.py startapp miapp**_

Esto crea un directorio llamado _miapp_. Dentro tenemos los diferentes ficheros de configuración _models.py_, _views.py_, ..., etc.
Las apps especifican en la lista _INSTALLED APPS_, dentro del fichero _settings.py_ en el directorio del proyecto. Vemos que automáticamente se ha añadido una app llamada _miapp_ al final de la lista INSTALLED_APPS dentro del fichero  _settings.py_ del proyecto:

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    _**'miapp'**_,
]

Vemos que con Django ya vienen utilidades por defecto, tales como: admin, auth, ..., etc.

## El fichero de utilidades _manage.py_:

Para consultar todas las funcionalidades del fichero _manage.py_, teclear el siguiente comando:

_**py manage.py help**_

Por ejemplo, para obtemer ayuda del arranque del servidor, teclearemos el comando:

_**py manage.py help runserver**_

## Instalación de Pylint

Pylint en un lintern de python. Existe un lintern específicamente para trabajar con Django. Se instala con el comando pip (en modo administrador):

_**pip install pylint-django**_

En Visual Code Studio podemos especificar  *pylint_django* en el setting: _python>linting>pylint path_ en *files>settings*

## Para hacer las migraciones

Para hacer las migraciones en los cambios en los modelos, vamos al directorio del proyecto y tecleamos:

_**py manage.py makemigrations**_

## Para generar automaticamente instrucciones de creación en SQL

Para generar automáticamente las instrucciones SQL para un nuevo modelo, teclear el comando:

_**py manage.py sqlmigrate miapp 0001**_ Donde 0001 es el número de la migración, (Efectuado en el párrafo anterior)

para que se ejecuten las instrucciones sql para la creación de la db, ejecutamos

_**py manage.py migrate**_

## Modificar el modelo

Una vez modificado el modelo (se modifican o se añaden/eliminan campos), teclear secuencialmente:

_**py manage.py makemigrations**_ Se crea, por ejemplo la versión 0002

_**py manage.py sqlmigrate miapp 0002**_ Con esto se crean las instrucciones sql de la modificación

_**py manage.py migrate**_ Para ejecutar la migración

## Panel de admnistración

Antes es necesario parar el servidor

_**py manage.py createsuperuser**_ Crea la cuenta de superusuario

Se arranca el servidor otra vez y se accede al panel del administración con la dirección https://localhost:8000/admin


_

## Enlaces

* [Master_en_Python]: Enlace al curso.
* [Udemy]: Enlace a Udemy.
* [Victor_Robles]: Enlace a la página web del profesor.
* [Wikipedia]: Django (Wikipedia).
* [Documentacion]: Documenteación de Django.

## Version

1.0.0 

## Authors

* **Luis Cárceles** - *Initial work* - [GitHub Timer]


[Master_en_Python]: https://victorroblesweb.es/2020/04/03/master-en-python-aprende-python-django-flask-tkinter-y-mas/
[Udemy]: https://www.udemy.com
[Victor_Robles]: https://victorroblesweb.es/
[Wikipedia]: https://es.wikipedia.org/wiki/Django_(framework)
[descarga]: https://www.djangoproject.com/download/
[Documentacion]: https://docs.djangoproject.com/en/3.0/

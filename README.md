Listado de rutas de carpetas
Estrcutura del proyecto
C:.
|   README.md
|   requirements.txt
|   
+---.vscode
|       settings.json
|       
\---CRUDprueba
    |   db.sqlite3
    |   manage.py
    |   
    +---CRUDprueba
    |   |   asgi.py
    |   |   settings.py
    |   |   urls.py
    |   |   wsgi.py
    |   |   __init__.py
    |   |   
    |   \---__pycache__
    |           settings.cpython-37.pyc
    |           urls.cpython-37.pyc
    |           wsgi.cpython-37.pyc
    |           __init__.cpython-37.pyc
    |           
    \---prueba
        |   admin.py
        |   apps.py
        |   filters.py
        |   forms.py
        |   models.py
        |   resources.py
        |   tests.py
        |   urls.py
        |   views.py
        |   __init__.py
        |   
        +---migrations
        |   |   0001_initial.py
        |   |   0002_auto_20210517_2250.py
        |   |   __init__.py
        |   |   
        |   \---__pycache__
        |           0001_initial.cpython-37.pyc
        |           0002_auto_20210517_2250.cpython-37.pyc
        |           __init__.cpython-37.pyc
        |           
        +---templates
        |       base.html
        |       clientes_form.html
        |       clientes_list.html
        |       importar.html
        |       
        \---__pycache__
                admin.cpython-37.pyc
                filters.cpython-37.pyc
                forms.cpython-37.pyc
                models.cpython-37.pyc
                resources.cpython-37.pyc
                urls.cpython-37.pyc
                views.cpython-37.pyc
                __init__.cpython-37.pyc


El proyectos se compone de una aplicación y la estrcutura genral de Django
se realiza con Python 3.7.2 y Django==3.0.2 como se puede comprobar en el archivo requirements.txt

Para ejecutar el proyecto descargue el codigo desde la ruta del repositorio.
Cree una maquina virtual en lo posible.
Instale virtaulenv o virtualenvwrapper, la primero opción le permite crear maquinas locales, la segun le permite crear una carpeta local y hacer administración de los entornos de desde CMD
verifique la documentacion segun su preferencia
https://edgardorl.com/blog/instalar-python-pip-y-virtualenv-en-windows-10/
https://virtualenvwrapper.readthedocs.io/en/latest/install.html

Instalacion de los componentes del proyecto:

Ejecute en la consola en la raiz del proyecto o en la ubicación del requirements.txt 
pip install -r requirements.txt 
para cargar las librerias

Una vez instaladas dirijase en la carpeta del projecto a :

cd Django-CRUD/CRUDprueba
y ejecute para crear las migramigraciones a la BBDD:

python manage.py makemigrations
python manage.py migrations

Ejecute para iniciar el proyecto:
python manage.py runserver


se presentara una imformación similar a esta:

System check identified no issues (0 silenced).
May 17, 2021 - 23:21:17
Django version 3.0.2, using settings 'CRUDprueba.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.


En el explorador, en la URL:
http://127.0.0.1:8000/prueba

Se encuentra la vista principal del proyecto, en la cual se pueden ver los clientes cargar nuevos clientes de manera manual o masiva y el Boton "back to list" que permite ver el listato con la barra de filtrado.

Actual mente el programa solo admite la carga de archivos en formato "xls" con los campos:

name_client','country','city','category'

finalice el trabajo con "ctrl+c"


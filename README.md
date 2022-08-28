# Django-MySQL-REST-API

REST API creada con Python, el framework web Django y el SGBD MySQL, con el protocolo HTTP y los método GET, POST, PUT y DELETE.

INSTALAR PYTHON3 !!!!!!  el comando depende de si es window o linux
INSTALAR PIP     !!!!!!  el comando depende de si es window o linux

pip install virtualenv *** INSTALAR LIBRERIA PARA MAQUINAS VIRTUALES

virtualenv -p python3 env *** PONER CONSOLA EN CARPETA DEL PROYECTO Y CREAR MAQUINA VIRTUAL

./env/Scripts/activate *** ACTIVAR MAQUINA VIRTUAL

pip install Django==3.2.4 *** INSTALAR DJANGO

pip list  *** VERIFICA LIBRERIAS INSTALADAS

django-admin startproject $NombreDelProyecto *** CREAR PROYECTO NUEVO (1)

django-admin startapp $NombreDeApi *** CREAR PRIMERA API
 
pip install mysqlclient pymysql *** INSTALAR CONECTORES MYSQL

pip install django-cors-headers *** INSTALAR LIBRERIA DE CORS


*****COLOCARSE EN LA CARPETA DEL PROYECTO (1) **************************************************

python manage.py makemigrations

python manage.py migrate

*****EJECUTAR SERVIDOR *************************************************************************

python manage.py runserver *** PARARSE EN LA CONSOLA EN LA CARPETA DEL PROYECTO (1)




### ENLACES DE SOPORTE PARA CORRER PROJECTO
   - https://www.youtube.com/watch?v=W530YJd3dUU&ab_channel=N1G1CHANNEL
   - https://bobcares.com/blog/oserror-mysql_config-not-found/

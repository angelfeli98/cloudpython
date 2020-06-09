# CLOUDPYTHON 

Proyecto para aplicaciones distribuidas

### Guia para usar el repositorio:

Si es la primera vez usando git lo instalamos en: https://git-scm.com/download/win

Crea tu cuenta en GitHub https://github.com/

Agrega tu usuario y contraseña a la configuracion de git usando el bash de git

```
git config --global user.name "your username"

git config --global user.password "your password"
```


### Si es la primera vez usando el repositorio :

Mandame tu correo para agregarte como colaborador en el proyecto

Asegurate de estar en ruta donde quieres que se descargue el repositorio

Una vez estes como colaborador ejecuta en el bash de git 
```
git init
```

Después ejecuta el comando
```
git clone https://github.com/angelfeli98/cloudpython.git
```
Esto creará una carpeta que es una copia del repositorio en tu computadora.


Ejecuta el siguiente comando 

```
git remote add SD https://github.com/angelfeli98/cloudpython.git
```

Una vez que terminando de trabajar ejecuta los siguientes comandos, todos dentro de la carpeta del proyecto

```
git add .
```

despues 

```
git commit -m "MENSAJE DE EJEMPLO"
```

y por ultimo 

```
git push SD master
```


### Para demás ocasiones que trabajes el proyecto

Colócate dentro de la carpeta del proyecto y actualiza tu repositorio local 
 
```
git pull SD
```

Una vez que terminando de trabajar ejecuta los siguientes comandos, todos dentro de la carpeta del proyecto

```
git add .
```

despues 

```
git commit -m "MENSAJE DE EJEMPLO"
```

y por ultimo 

```
git push SD master
```

## GUIA PARA EJECUTAR EL PROYECTO DE DJANGO

Verificar que este instalado python en tu equipo 

```
python --version 
```
Deberias de tener el siguiente resultado

```
Python "version"
```

De no ser asi descargarlo en https://www.python.org/

Una vez descargado e instalado ejecutamos 

```
pip install Django
```

Para correr el proyecto necesitaras las siguientes dependenciad pip

-pillow
-cryptography
-django-ckeditor

Para instalar un comando ejecuta la siguiente dependencia
```
pip install nombreDependencia
```

Para ejecutar correr el proyecto no colocamos donde se encuentre el archivo manage.py

Ejecutamos 

```
python manage.py runserver
```

## GUIA SI VAS A MODIFICAR LOS MODELOS DE LA BASE DE DATOS 

Una vez modificados los modelos ejecutamos 

```
python manage.py makemigrations 
```
Despues 

 ```
python manage.py sqlmigrate nombreApp version
 ```
 Donde version la puedes ver en la carptea Migrations 

 Despues 
  ```
python manage.py migrate 
  ```



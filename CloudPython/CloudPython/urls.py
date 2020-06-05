"""CloudPython URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from proyectos import views as proyecto
from usuarios import views as user

urlpatterns = [
    path('admin/', admin.site.urls, name = 'admin'),
    path('', proyecto.index , name = "index"), 
    path('proyectos-destacados/', proyecto.proyectos, name = 'proyectos'),
    path('register/', user.signup, name = 'register'),
    path('register-user/', user.guardarUsuarios, name = 'Guardar'),
    path('proyect/', proyecto.proyecto, name = 'proyecto'),
    path('login/', user.login, name = "login"),
    path('loged/', user.loge, name = 'loged'),
    path('loge/', user.indexUser, name = 'indexLoged'),
    path('proyects-des', user.proyectosUser, name = 'proyectosLoged'),
]

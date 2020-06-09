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
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls, name = 'admin'),
    path('', proyecto.index , name = "index"), 
    path('proyectos-destacados/', proyecto.proyectos, name = 'proyectos'),
    path('register/', user.signup, name = 'register'),
    path('register-user/', user.guardarUsuarios, name = 'Guardar'),
    path('proyect/<int:idP>', proyecto.proyecto, name = 'proyecto'),
    path('proyect/', proyecto.proyecto, name = 'proyecto'),
    path('login/', user.login, name = "login"),
    path('loged/', user.loge, name = 'loged'),
    path('loge/', user.indexUser, name = 'indexLoged'),
    path('proyects-des/<str:User>/', user.proyectosUser, name = 'proyectosLoged'),
    path('proyects-des/<str:User>/<int:idP>', user.proyectosUser, name = 'proyectosLoged'),
    path('proyect-loged/<str:idUser>/<int:idP>', user.proyectoUser, name = 'proyectoLoged'),
    path('proyect-loged/<str:idUser>', user.proyectoUser, name = 'proyectoLoged'),
    path('your-proyects/<str:User>', proyecto.yourProyects, name = 'tusproyectos'),
    path('register-proyec/<str:User>', proyecto.newproyect, name = 'newproyect'),
    path('save-proyect/<str:User>', proyecto.savePoryect, name = 'saveproyecto'),
    path('form-reset', user.recuperarpass, name = 'formreset'),
    path('send-email/', user.sendEmail, name = 'send_email'),
    path('reset-pass/<str:User>', user.newpass, name = 'newpass'),
    path('new-pass/<str:idUser>', user.changePass, name = 'formpass'),
    path('loge/<str:User>', user.indexUser, name = 'indexLogedUser'),
    path('proyectos-destacados/<int:idP>', proyecto.proyectos, name = 'proyectos'),
    path('form-suport/<str:user>/<int:idP>', proyecto.formSuport, name = 'formsuport'),
    path('proyect-suport/<int:user>/<int:idP>', proyecto.suportProyect, name = 'suport'),
    path('user-info/<str:user>', proyecto.userInfo, name = 'userinfo'),
    path('proyects-categoria/', proyecto.proyectosCategorias, name = 'proyectsCate'),
    path('proyects-categoria/<int:idC>', proyecto.proyectosCategorias, name = 'proyectsCate'),
    path('proyects-categoria/<str:user>/<int:idC>', proyecto.proyectosCategorias, name = 'proyectsCate'),
]

# Configuracion para cargar imagenes 

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

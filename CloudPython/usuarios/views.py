from django.shortcuts import render, HttpResponse, redirect
from usuarios.forms import UsuariosForm 
from proyectos import templates
import random
from usuarios.models import User
# Create your views here.

def signup(request):
    form = UsuariosForm()

    return render(request, 'signup.html', {
        'form' : form
    })

def index(request):

    return HttpResponse("Adios")

def guardarUsuarios(request):
    
    try: 
        user = request.POST['user']
        name = request.POST['name']
        password = request.POST['password']
        photo = request.POST['image']
        wallet = random.randint(0, 12000)

        item = User(
            user = user,
            name = name,
            password = password,
            photo = photo,
            wallet = wallet
        )

        item.save()

        return HttpResponse("Usuario Guardado")
    except:
        return HttpResponse("Error")

    
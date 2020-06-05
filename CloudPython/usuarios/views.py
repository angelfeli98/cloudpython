from django.shortcuts import render, HttpResponse, redirect
from usuarios.forms import UsuariosForm 
from proyectos import templates
import random
from usuarios.models import User
from cryptography.fernet import Fernet



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
        conPassword = request.POST['conPassword']
        photo = request.POST['image']
        wallet = random.randint(0, 12000)
        
        if not (password == conPassword):
            form = UsuariosForm()
            return render(request, 'signup.html', {
                'form' : form,
                'message' : "Las contraseñas no coinciden" 
            })
        #key = Fernet.generate_key()

        file = open('key.key', 'rb+')
        key = file.read()
        file.close()
        
        f = Fernet(key)
        passwordb = password.encode()

        passwdencry = f.encrypt(passwordb)

        item = User(
            user = user,
            name = name,
            password = passwdencry,
            photo = photo,
            wallet = wallet
        )

        item.save()
        flag = item

        return render(request, 'signup-su.html', {
            'User' : flag
        })
    except:
        return HttpResponse("Error")


    
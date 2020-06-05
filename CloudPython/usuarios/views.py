from django.shortcuts import render, HttpResponse, redirect
from usuarios.forms import UsuariosForm, LoginUser 
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
        print(key)
        

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
    except Exception as e:
        form = UsuariosForm()
        return render(request, 'signup.html', {
                'form' : form,
                'message' : "Usuario o Contraseña ya utilizada" 
            })


def login(request):
    form = LoginUser()
    return render(request, 'login.html',{
        'form' : form
    })  

def loge(request):

    try:
        user = request.POST['user']
        password = request.POST['password']

        user_ver = User.objects.filter(user = user)
        
        if not (user_ver):
            bandera = False
        else:
            file = open('key.key', 'rb+')
            key = file.read()
            file.close()
        
            f = Fernet(key)
            passwordd = f.decrypt(user_ver[0].password).decode()
            if passwordd == password:
                return render(request, 'index.html', {
                    'User' : user_ver[0]
                })
            else:
                form = LoginUser()
                message = "Usuario o Contraseña incorrecto"
                return render(request, 'login.html', {
                    'form' : form,
                    'message': message
                })   
    except:
        return HttpResponse("ERROR")
    return HttpResponse("Login")


def indexUser(request):
    if request.POST:
        user = User(request.POST)

    return render(request, 'index.html', {
        'User' : user
    })

def proyectosUser(request):
    if request.GET:
        user = User(request.GET)

    return render(request, 'proyectos.html', {
        'User' : user
    })
from django.shortcuts import render, HttpResponse, redirect
from usuarios.forms import UsuariosForm, LoginUser, SendMail, ResetPass 
from proyectos import templates
import random
from usuarios.models import User
from cryptography.fernet import Fernet
from django.contrib import messages
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.http.request import QueryDict




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
        send_mail(
            'WELLCOME TO FOUND.ME {}'.format(name),
            'AHORA ERES PARTE DE UNA COMUNIDAD QUE BUSCA HACER LOS SUEÑOS REALIDAD',
            'founde.me@gmail.com',
            [user],
            fail_silently=False,
        )
        item.save()
        
        flag = item
        form = UsuariosForm()
        return render(request, 'signup-su.html', {
            'User' : flag,
            'form' : form
        })
    except Exception as e:
        form = UsuariosForm()
        print(type(e).__name__)
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
                messages.success(request,'Bienvenido de nuevo {}'.format(user_ver[0].name))
                return render(request, 'index.html', {
                    'User' : user_ver[0],
                })
            else:
                form = LoginUser()
                message = "Usuario o Contraseña incorrecto"
                return render(request, 'login.html', {
                    'form' : form
                })   
    except:
        return HttpResponse("ERROR")
    return HttpResponse("Login")


def indexUser(request):
    if request.POST:
        user = User(request.POST)
        request.POST = None
    elif request.GET:
        user = User(request.GET)
        
    print(request)
    return render(request, 'index.html', {
        'User' : user
    })

def proyectosUser(request):
    if request.GET:
        user = User(request.GET)
    
    return render(request, 'proyectos.html', {
        'User' : user
    })

def proyectoUser(request):
    if request.GET:
        user = User(request.GET)
 
    return render(request, 'proyect.html', {
        'User' : user
    })

def recuperarpass(request):
    form = SendMail()

    return render(request, 'recuperar_pass.html',{
        'form' : form
    })

def sendEmail(request):
    try:
        if request.POST:
            user = User.objects.filter(user = request.POST['user'])
            if user:
                send_mail(
                'RESET PASSWORD',
                'Entra al siguiente enlace para recuperar tu contraseña http://127.0.0.1:8000/reset-pass/?{}'.format(user),
                'founde.me@gmail.com',
                [request.POST['user']],
                fail_silently=False,
                )
                messages.success(request,'Te hemos enviado un email para cambiar tu contraseña')
                return render(request, 'index.html')
            else:
                form = SendMail()
                message = "No hay ningun usuario con este email"
                return render(request, 'recuperar_pass.html', {
                    'form' : form,
                    'message' : message
                })  
    except:
        pass

    form = SendMail()
    return render(request, 'recuperar_pass.html',{
        'form' : form
    })

def newpass(request):
    if request.GET:
        print(request.GET.keys())
    form = ResetPass()
    return render(request, 'newpassword.html',{
        'form' : form
    })

def changePass(request):
    if request.POST:
        print(request.POST)

    messages.success(request,'Bienvenido de nuevo {}'.format())
    return render(request, 'index.html')




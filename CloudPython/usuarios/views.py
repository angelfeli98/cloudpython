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
from proyectos.models import Proyect




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
        idUser = User.objects.filter(user = user)[0].id
        flag = item
        form = UsuariosForm()
        return render(request, 'signup-su.html', {
            'User' : flag,
            'form' : form,
            'idUser' : 'sssfcv{}sqaznchdyr'.format(idUser),
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
                proyectos_destacado = Proyect.objects.all()[:3]
                messages.success(request,'Bienvenido de nuevo {}'.format(user_ver[0].name))
                return render(request, 'index.html', {
                    'User' : 'sssfcv{}sqaznchdyr'.format(user_ver[0].id),
                    'proys' : proyectos_destacado
                })
            else:
                form = LoginUser()
                message = "Usuario o Contraseña incorrecto"
                return render(request, 'login.html', {
                    'form' : form,
                    'message' : message 
                })   
    except Exception as e:
        return HttpResponse(type(e).__name__)
    return HttpResponse("Login")


def indexUser(request, User = ''):
    if request.POST:
        pass

    elif request.GET:
        user = User

    proyectos_destacado = Proyect.objects.all()[:3]

    return render(request, 'index.html',{
        'proys' : proyectos_destacado,
        'User' : User
    })
        

def proyectosUser(request, User = '', idP = 0):
    proyectos_destacado = Proyect.objects.all()[:3]
    return render(request, 'proyectos.html', {
        'User' : User,
        'proys' : proyectos_destacado,
    })

def proyectoUser(request, idUser = '', idP = 0):
    aux = ''
    for letra in idUser:
        if letra.isdigit():
            aux += letra

    id_user = int(aux) 
    
    proyecto = Proyect.objects.get(pk = idP)
    
    owner = User.objects.get(pk = proyecto.userOwner_id)

    if id_user == owner.id:
        mine = True
    else:
        mine = False

    return render(request, 'proyect.html', {
        'proyecto' : proyecto,
        'Owner' : owner,
        'User' : idUser,
        'Mine' : mine
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
                try:
                    send_mail(
                    'RESET PASSWORD',
                    'Entra al siguiente enlace para recuperar tu contraseña http://127.0.0.1:8000/reset-pass/sssfcv{}sqaznchdyr'.format(user[0].id),
                    'founde.me@gmail.com',
                    [request.POST['user']],
                    fail_silently=False,
                    )
                    messages.success(request,'Te hemos enviado un email para cambiar tu contraseña')
                    proyectos_destacado = Proyect.objects.all()[:3]

                    return render(request, 'index.html',{
                        'proys' : proyectos_destacado
                    })
                except:
                    form = SendMail()
                    message = "Ocurrio un error"
                    return render(request, 'recuperar_pass.html', {
                    'form' : form,
                    'message' : message
                })  

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

def newpass(request, User):
    
    form = ResetPass()
    return render(request, 'newpassword.html',{
        'form' : form,
        'User' : User
    })

def changePass(request, idUser):
    aux = ''
    for letra in idUser:
        if letra.isdigit():
            aux += letra

    id_user = int(aux) 
    user = User.objects.get(pk = id_user)

    if request.POST:
        newpass = request.POST['newpass']
        conpass = request.POST['conPassword']
        if not (newpass == conpass):
            form = ResetPass()
            
            return render(request, 'newpassword.html',{
                'form' : form,
                'User' : id_user,
                'message' : "No coinciden las contraseñas" 
            })
        #key = Fernet.generate_key()

        file = open('key.key', 'rb+')
        key = file.read()
        file.close()
        
        f = Fernet(key)
        passwordb = newpass.encode()
        passwdencry = f.encrypt(passwordb)
        try:
            user.password = passwdencry
            user.save()
        except:
            return HttpResponse("ERROR")
    proyectos_destacado = Proyect.objects.all()[:3]
    messages.success(request,'Bienvenido de nuevo {}'.format(user.name))
    return render(request, 'index.html', {
        'User' : 'sssfcv{}sqaznchdyr'.format(user.id),
        'proys' : proyectos_destacado
    })




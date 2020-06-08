from django.shortcuts import render, HttpResponse, redirect
from proyectos.forms import ProyectoSave, SuportProyect
from datetime import date, datetime
from proyectos.models import Proyect, Category, Patron
from usuarios.models import User
from django.contrib import messages
# Create your views here.

def index(request):
    proyectos_destacado = Proyect.objects.all()[:3]

    return render(request, 'index.html',{
        'proys' : proyectos_destacado
    })

def proyectos(request, idP = ''):
    proyectos_destacado = Proyect.objects.all()[:3]
    return render(request, 'proyectos.html',{
        'proys' : proyectos_destacado
    })

def proyecto(request, idP = ''):
    proyecto = Proyect.objects.get(pk = idP)
    owner = User.objects.get(pk = proyecto.userOwner_id)
    patrons = len(Patron.objects.filter(proyecto_id = idP))
    return render(request, 'proyect.html', {
        'proyecto' : proyecto,
        'Owner' : owner,
        'NoP' : patrons
    })

def yourProyects(request, User):
    aux = ''
    for letra in User:
        if letra.isdigit():
            aux += letra

    userOwner_id = int(aux) 
    proyects = Proyect.objects.filter(userOwner_id = userOwner_id)
    if request.GET:
        user = request.GET
    return render(request, 'yourproyects.html', {
        'User' : User,
        'proyects' : proyects
    })

def newproyect(request, User):
    form = ProyectoSave()
    
    return render(request, 'newproyect.html', {
        'form' : form,
        'User' : User
    })

def savePoryect(request, User):
    aux = ''
    for letra in User:
        if letra.isdigit():
            aux += letra

    userOwner_id = int(aux) 

    if request.POST:
        try:
            name = request.POST['name']  
            goal = request.POST['goal']
            deadline = request.POST['deadline']
            description = request.POST['description']
            image = request.POST['image']
            category_id  = request.POST['category']
            actual = 0
            deadline = datetime.strptime(deadline, '%Y-%m-%d').date()
        

            data = Proyect(
                name = name,  
                goal = goal,
                deadline = deadline,
                description = description,
                image = image,
                category_id  = category_id,
                actual = actual,
                userOwner_id = userOwner_id,
            )

            data.save()

            proyects = Proyect.objects.filter(userOwner_id = userOwner_id,)
            
            return render(request, 'yourproyects.html', {
                'User' : User,
                'proyects' : proyects
            })
        except Exception as e:
            form = ProyectoSave()
            return render(request, 'newproyect.html', {
                'form' : form,
                'User' : User
            })


    else:
        form = ProyectoSave()
        return render(request, 'newproyect.html', {
        'form' : form,
        #'User' : user
        })
        
def formSuport(request, user = '', idP = 0):
    form = SuportProyect()
    aux = ''
    for letra in user:
        if letra.isdigit():
            aux += letra
    idUser = int(aux) 
    
    userdata = User.objects.get(pk = idUser)
    return render(request, 'suport-p.html', {
        'form' : form,
        'User' : userdata,
        'proyect' : idP,
    })

def suportProyect(request, user  = 0, idP = 0):
    
    if request.POST:
        money = request.POST['money']
        userp = User.objects.get(pk = user)
        form = SuportProyect()
        if float(money) > userp.wallet:
            message = "No tienes tanto dinero"
            return render(request, 'suport-p.html', {
            'form' : form,
            'User' : userp,
            'proyect' : idP,
            'message' : message
        })
        else:
            if float(money) >= 0:
                proyecto = Proyect.objects.get(pk = idP)
                proyecto.actual += float(money)
                proyecto.save()
                beneficiario = User.objects.get(pk = proyecto.userOwner_id)
                beneficiario.wallet += float(money)
                beneficiario.save() 
                userp.wallet -= float(money)
                userp.save()
                patron = Patron(
                    patron_id = userp.id,
                    proyecto_id = idP
                )
                patron.save()
                patrons = len(Patron.objects.filter(proyecto_id = idP))
            
                messages.success(request,'Gracias por apoyar proyectos {}'.format(userp.name))
                return render(request, 'proyect.html',{
                    'User' : 'sssfcv{}sqaznchdyr'.format(userp.id),
                    'idP' : idP, 
                    'proyecto' : proyecto,
                    'NoP' : patrons
                })
            else:
                message = "La cifra debe de ser positiva"
                return render(request, 'suport-p.html', {
                'form' : form,
                'User' : userp,
                'proyect' : idP,
                'message' : message
                })



    return HttpResponse('Apoyado')


def userInfo(request, user):
    aux = ''
    for letra in user:
        if letra.isdigit():
            aux += letra
    idUser = int(aux) 
    userinfo = User.objects.get(pk = idUser) 
    return render(request, 'user-info.html', {
        'User' : userinfo
    })



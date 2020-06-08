from django.shortcuts import render, HttpResponse, redirect
from proyectos.forms import ProyectoSave 
from datetime import date, datetime
from proyectos.models import Proyect
from usuarios.models import User
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

    return render(request, 'proyect.html', {
        'proyecto' : proyecto,
        'Owner' : owner,
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
        


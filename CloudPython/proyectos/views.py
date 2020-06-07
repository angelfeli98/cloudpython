from django.shortcuts import render, HttpResponse, redirect
from proyectos.forms import ProyectoSave 
from datetime import date, datetime
from proyectos.models import Proyect
# Create your views here.

def index(request):
    if request.GET:
        user = request.GET
       
    return render(request, 'index.html')

def proyectos(request, User = ''):

    return render(request, 'proyectos.html',{
        'User' : User 
    })

def proyecto(request):

    return render(request, 'proyect.html')

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
        


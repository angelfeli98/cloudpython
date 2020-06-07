from django.shortcuts import render, HttpResponse, redirect
from proyectos.forms import ProyectoSave 
from datetime import date, datetime
from proyectos.models import Proyect
# Create your views here.

def index(request):
    if request.GET:
        user = request.GET
       
    return render(request, 'index.html')

def proyectos(request):

    return render(request, 'proyectos.html')

def proyecto(request):

    return render(request, 'proyect.html')

def yourProyects(request):
    if request.GET:
        user = request.GET
    return render(request, 'yourproyects.html', {
        'User' : user
    })

def newproyect(request):
    form = ProyectoSave()
    user = request.GET.keys()
    return render(request, 'newproyect.html', {
        'form' : form,
        'User' : user
    })

def savePoryect(request):

    if request.POST:
        try:
            name = request.POST['name']  
            goal = request.POST['goal']
            deadline = request.POST['deadline']
            description = request.POST['description']
            image = request.POST['image']
            category_id  = request.POST['category']
            actual = 0
            userOwner_id = 4
            deadline = datetime.strptime(deadline, '%Y-%m-%d').date()
            print(type(deadline))
            print(deadline)

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
            
            return HttpResponse('SALVADO')
        except Exception as e:
            return HttpResponse(type(e).__name__)


    else:
        form = ProyectoSave()
        return render(request, 'newproyect.html', {
        'form' : form,
        #'User' : user
        })
        


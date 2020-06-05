from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    if request.GET:
        user = request.GET
        print(user)

    return render(request, 'index.html')

def proyectos(request):

    return render(request, 'proyectos.html')

        


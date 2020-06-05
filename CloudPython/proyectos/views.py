from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):

    return render(request, 'index.html')

def proyectos(request):

    return render(request, 'proyectos.html')

        


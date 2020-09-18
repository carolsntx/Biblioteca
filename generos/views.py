from django.shortcuts import render
from .models import Genero


def genero(request):
    genero = Genero.objects.all()
    return render(request, 'generos.html', {'genero': genero})

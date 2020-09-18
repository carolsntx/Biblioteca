from django.shortcuts import render
from .models import Livros

def index(request):
    livros = Livros.objects.all()
    return render(request, 'index.html', {'livros': livros})
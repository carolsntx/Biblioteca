from django.shortcuts import render
from .models import Autor

def autor(request):
    autor = Autor.objects.all()
    return render(request, 'autores.html', {'autor': autor})

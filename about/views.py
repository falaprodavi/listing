from django.shortcuts import render
from about.models import About
from estabelecimentos.models import Categoria

def about(request):    
    categorias = Categoria.objects.all()
    abouts = About.objects.last()   
    return render(request, 'about.html', {
        'abouts' : abouts,         
        'categorias' : categorias,         
        })

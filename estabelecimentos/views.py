from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from banner.models import Banner
from estabelecimentos.models import Cidade, Categoria, Estabelecimento
from django.db.models import Q

# Create your views here.
def home(request):    
    banners = Banner.objects.last()
    categorias = Categoria.objects.all()
    cidades = Cidade.objects.all()              
    return render(request, 'home.html', {'banners' : banners, 'categorias': categorias, 'cidades' : cidades})

def explore(request):      
    res = Estabelecimento.objects.all()     
    
    keywords = request.GET.get('keywords', "")
    cidade = request.GET.get('cidade', "")
    categoria = request.GET.get('categoria', "")  
    
    estabelecimentos = res.filter(
        (Q(descricao__icontains=keywords) |
         Q(nome__icontains=keywords)),
    )    
    try:
        if isinstance(int(categoria), int):
            estabelecimentos = estabelecimentos.filter(categoria=categoria)
    except Exception:
        pass
    try:
        if isinstance(int(cidade), int):
            estabelecimentos = estabelecimentos.filter(cidade=cidade)
    except Exception:
        pass
        
    context = {
        'cidades': Cidade.objects.all(),
        'categorias': Categoria.objects.all(),
        'estabelecimentos': estabelecimentos,
        'values': request.GET
    }    
    return render(request, 'explore.html', context)

def estabelecimento(request, slug):
    estabelecimento = get_object_or_404(Estabelecimento, slug=slug)
    return render (request, 'estabelecimento.html', {'estabelecimento' : estabelecimento})
    
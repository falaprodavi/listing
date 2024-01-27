from django.shortcuts import render

from banner.models import Banner
from estabelecimentos.models import Categoria, Cidade, Estabelecimento

# Create your views here.

def banner(request):
    return render(request, 'banner.html')
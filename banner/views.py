from django.shortcuts import render

from banner.models import Banner

# Create your views here.

def banner(request):
    return render(request, 'banner.html')

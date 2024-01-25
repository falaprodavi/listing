from django.shortcuts import render

from banner.models import Banner

# Create your views here.
def home(request):
    banners = Banner.objects.get()
    return render(request, 'home.html', 
                  {'banners' : banners}
                  )
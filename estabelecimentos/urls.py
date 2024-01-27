from django.urls import path, re_path
from . import views

urlpatterns = [
path('', views.home, name="home"),
path('home/', views.home, name="home"),
path('explore/', views.explore, name="explore"),
path('<slug:slug>', views.estabelecimento, name="estabelecimento"),
]
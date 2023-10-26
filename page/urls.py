from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home),

    path('signin', views.signIn),
    path('login', views.logIn),

    path('inicio', views.inicio),

    path('torneos', views.torneos),
    path('partidos', views.partidos),

    path('perfil', views.perfil),

]
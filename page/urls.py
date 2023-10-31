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
    path('ranking', views.ranking),

    path('torneo1', views.torneo1),
    path('cambiar_numero', views.cambiar_numero, name='cambiar_numero'),

]
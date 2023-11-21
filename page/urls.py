from django.urls import path
from . import views
from django.conf import settings
from .views import postListView, PostDetailView

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home),

    path('signin', views.signIn),
    path('login', views.logIn),
    path('logout', views.salirSesion),

   

    path('torneos', views.torneos),
    path('partidos', views.partidos),

    path('perfil', views.perfil),
    path('ranking', views.ranking),

    path('torneo1', views.torneo1),
    path('cambiar_numero', views.cambiar_numero, name='cambiar_numero'),

   
    path('inicio', postListView.as_view(), name='inicio'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='detalle_post'),
]
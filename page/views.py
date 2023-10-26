from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def signIn(request):
    return render(request, 'registro.html')

def logIn(request):
    return render(request, 'login.html')

def inicio(request):
    return render(request, 'pagInicial.html')

def torneos(request):
    return render(request, 'torneos.html')

def partidos(request):
    return render(request, 'partidos.html')

def perfil(request):
    return render(request, 'perfil.html')

def ranking(request):
    return render(request, 'ranking.html')
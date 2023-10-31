from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from .models import Numero
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


# Create your views here.

def home(request):
    return render(request, 'home.html')

def signIn(request):
    if request.method=='GET':
        return render(request, 'registro.html', {'form' : UserCreationForm})
    else:
        if request.POST["password1"]!=request.POST["password2"]:
            return render(request, 'registro.html', {'form' : UserCreationForm, 'error':'Las contraseñas no coinciden'})
        else:
            name = request.POST["username"]
            password = request.POST["password1"]
            user = User.objects.create_user(username=name, password=password)
            user.save()
            return render(request, 'registro.html', {'form' : UserCreationForm, 'error':'Usuario Registrado!'})

def logIn(request):
    if request.method=='GET':
        return render(request, 'login.html',{ 'form' : AuthenticationForm})
    else:
        name = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=name, password=password)
        if user is None:
            return render(request, 'login.html', {'form' : AuthenticationForm, 'error':'Usuario o contraseña incorrectos'})
        else:
            return redirect('/inicio')

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

def torneo1(request):
    numero = Numero.objects.first()
    return render(request, 'torneo1.html', {'numero': numero});


def cambiar_numero(request):
    # Acceso al objeto request
    if request.method == 'POST':
        # Tu lógica aquí
        numero = Numero.objects.first()
        numero.valor += 1
        numero.save()
        return JsonResponse({'nuevo_numero': numero.valor})
    else:
        return JsonResponse({'error': 'Método no permitido'})


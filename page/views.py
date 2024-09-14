from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse_lazy
from .models import Numero, Post, Partido
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django import forms
from django.views.generic import FormView
import requests
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
            login(request, user)
            return redirect('/inicio')

@login_required
def inicio(request):
    contexto = {
        'posts': Post.objects.all()
    }
    return render(request, 'pagInicio.html', contexto)

def salirSesion(request):
    logout(request)
    return redirect('/home')

def torneos(request):
    return render(request, 'torneos.html')

def partidos(request):
    partidos = Partido.objects.all()
    return render(request, 'partidos.html', {'partidos': partidos})


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



# POSTS --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


class postListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'pagInicio.html'
    context_object_name = 'posts'
    ordering = ['-fecha_creacion']


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post_detail.html' 


class PostCreateView(LoginRequiredMixin, CreateView ):
    model = Post
    fields = ['titulo', 'contenido']
    template_name = 'post_form.html' 

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['titulo', 'contenido']
    template_name = 'post_form.html'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.autor:
            return True
        return False
    

class PostDeleteView(DeleteView):
    model = Post
    success_url = '/inicio'
    template_name = 'post_confirm_delete.html'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.autor:
            return True
        return False
    
# PARTIDOS --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



class PartidoForm(forms.ModelForm):
    class Meta:
        model = Partido
        fields = ['nombre', 'descripcion', 'arbitro', 'exp', 'tipo', 'imagenUrl', 'fecha_creacion']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)




""" def mi_vista_para_el_formulario(request):


    if request.method == 'POST':
        form = PartidoForm(request.POST, request.FILES)
        if form.is_valid():
            # Procesa el formulario si es válido
            form.save()
            # Redirige a una página de éxito o haz lo que necesites hacer
    else:
        form = PartidoForm()

        
    
    return render(request, 'partido_form.html', {'form': form}) """

def mi_vista_para_el_formulario(request):
    if request.method == 'POST':
        form = PartidoForm(request.POST, request.FILES)
        if form.is_valid():
            partido = form.save(commit=False)
            partido.autor = request.user  # Asignar el usuario actual al campo 'autor'
            partido.save()
            return redirect('detalle_partido', pk=partido.pk)
            # Redirigir a una página de éxito o realizar otras acciones necesarias  # Reemplaza 'pagina_exito' con la URL correspondiente
    else:
        form = PartidoForm()
    
    return render(request, 'partido_form.html', {'form': form})

#Listar mis partidos

def listar_mis_partidos(request):
    # Obtén todos los partidos asociados al usuario actualmente autenticado
    partidos = Partido.objects.filter(autor=request.user)
    
    return render(request, 'mis_partidos.html', {'partidos': partidos})


#Detalles partidos

class PartidoDetailView(LoginRequiredMixin, DetailView):
    model = Partido
    template_name = 'partido_detail.html' 


class PartidoDeleteView(DeleteView):
    model = Partido
    success_url = '/partidos'
    template_name = 'partido_delete.html'

    def test_func(self):
        partido = self.get_object()
        if self.request.user == partido.autor:
            return True
        return False



def valorar(request):
    return render(request, 'valoracion.html')



def home(request):
    import requests
    
    api_key = '4b83531b0b9d4c49ab833956242504'  # Reemplaza esto con tu API key de WeatherAPI
    city = 'Santiago'  # Cambia a la ciudad deseada
    url = f'https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'
    response = requests.get(url)
    data = response.json()

    # Traducciones de las condiciones del clima
    condition_translations = {
        'Sunny': 'Soleado',
        'Partly cloudy': 'Parcialmente nublado',
        'Cloudy': 'Nublado',
        'Overcast': 'Cubierto',
        'Mist': 'Neblina',
        'Patchy rain possible': 'Posibilidad de lluvia',
        'Patchy snow possible': 'Posibilidad de nieve',
        'Patchy sleet possible': 'Posibilidad de aguanieve',
        'Patchy freezing drizzle possible': 'Posibilidad de llovizna helada',
        'Thundery outbreaks possible': 'Posibilidad de tormentas',
        'Blowing snow': 'Viento con nieve',
        'Blizzard': 'Tormenta de nieve',
        'Fog': 'Niebla',
        'Freezing fog': 'Niebla helada',
        'Patchy light drizzle': 'Llovizna ligera',
        'Light drizzle': 'Llovizna',
        'Freezing drizzle': 'Llovizna helada',
        'Heavy freezing drizzle': 'Llovizna helada intensa',
        'Patchy light rain': 'Lluvia ligera',
        'Light rain': 'Lluvia',
        'Moderate rain at times': 'Lluvia moderada',
        'Moderate rain': 'Lluvia moderada',
        'Heavy rain at times': 'Lluvia intensa',
        'Heavy rain': 'Lluvia intensa',
        'Light freezing rain': 'Lluvia helada ligera',
        'Moderate or heavy freezing rain': 'Lluvia helada moderada o intensa',
        'Light sleet': 'Aguanieve ligera',
        'Moderate or heavy sleet': 'Aguanieve moderada o intensa',
        'Patchy light snow': 'Nieve ligera',
        'Light snow': 'Nieve ligera',
        'Patchy moderate snow': 'Nieve moderada',
        'Moderate snow': 'Nieve moderada',
        'Patchy heavy snow': 'Nieve intensa',
        'Heavy snow': 'Nieve intensa',
        'Ice pellets': 'Granizo',
        'Light rain shower': 'Chubasco ligero',
        'Moderate or heavy rain shower': 'Chubasco moderado o intenso',
        'Torrential rain shower': 'Chubasco torrencial',
        'Light sleet showers': 'Aguanieve ligera',
        'Moderate or heavy sleet showers': 'Aguanieve moderada o intensa',
        'Light snow showers': 'Nieve ligera',
        'Moderate or heavy snow showers': 'Nieve moderada o intensa',
        'Light showers of ice pellets': 'Chubascos de granizo ligero',
        'Moderate or heavy showers of ice pellets': 'Chubascos de granizo moderados o intensos',
        'Patchy light rain with thunder': 'Lluvia ligera con truenos',
        'Moderate or heavy rain with thunder': 'Lluvia moderada o intensa con truenos',
        'Patchy light snow with thunder': 'Nieve ligera con truenos',
        'Moderate or heavy snow with thunder': 'Nieve moderada o intensa con truenos'
    }

    # Verificar si 'current' está presente en los datos recibidos
    if 'current' in data:
        current_weather = data['current']
        condition_text = current_weather['condition']['text']
        # Traducir la condición del clima si está en las traducciones, de lo contrario, mantenerla igual
        condition_text_translated = condition_translations.get(condition_text, condition_text)

        weather_data = {
            'icon_url': current_weather['condition']['icon'],  # La URL del ícono ya está proporcionada por la API
            'location': data['location']['name'],  # Nombre de la ciudad
            'temperature': current_weather['temp_c'],  # Temperatura en Celsius
            'condition_text': condition_text_translated  # Descripción del clima traducida
        }
    else:
        # Manejar el caso en que no se reciban datos del clima correctamente
        weather_data = {
            'icon_url': '',
            'location': 'N/A',
            'temperature': 'N/A',
            'condition_text': 'No disponible'
        }

    return render(request, 'home.html', {'weather_data': weather_data})

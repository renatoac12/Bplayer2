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









from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Numero(models.Model):
    valor = models.IntegerField(default=0)

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
        
    def get_absolute_url(self):
        return reverse('detalle_post', kwargs={'pk': self.pk})
    

class Partido(models.Model):
    SÍ = 'Sí'
    NO = 'No'
    DOBLES = 'Dobles'
    INDIVIDUAL = 'Individual'

    ARBITRO_CHOICES = [
        (SÍ, 'Sí'),
        (NO, 'No'),
    ]

    EXP_CHOICES = [
        (SÍ, 'Sí'),
        (NO, 'No'),
    ]

    TIPO_CHOICES = [
        (DOBLES, 'Dobles'),
        (INDIVIDUAL, 'Individual'),
    ]



    
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    arbitro = models.CharField(max_length=3, choices=ARBITRO_CHOICES, default=SÍ)
    exp = models.CharField(max_length=3, choices=EXP_CHOICES, default=SÍ)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default=INDIVIDUAL)
    imagenUrl = models.ImageField(upload_to='static/img')
    fecha_creacion = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
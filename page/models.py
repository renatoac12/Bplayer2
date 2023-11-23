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
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    arbitro = models.TextChoices('Sí', 'No')
    exp = models.TextChoices('Sí', 'No')
    imagenUrl = models.ImageField(upload_to='static/img')
    fecha_creacion = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nombre
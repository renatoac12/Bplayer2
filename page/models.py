from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


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
        
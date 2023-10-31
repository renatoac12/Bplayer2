from django.db import models

# Create your models here.

class Numero(models.Model):
    valor = models.IntegerField(default=0)


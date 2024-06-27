# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class Grupo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    token = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Usuario(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    rol = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name='usuarios', null=True, blank=True)
    
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    
    def __str__(self):
        return "Usuario: " + str(self.username)

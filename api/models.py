from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    username      = models.CharField(unique=True)
    email         = models.EmailField()
    password      = models.CharField()
    rol           = models.CharField()
    departamento  = models.CharField()
    
    USERNAME_FIELD = 'username'
    EMAIL_FIELD    = 'email'
    def __str__(self):
        return "Usuario: " + str(self.username)
from django.db import models

# Create your models here.

class Persona(models.Model):
    rut = models.CharField(max_length=11, unique=True)
    nombre = models.CharField(max_length=50)
    
    def __str__(self): #Nos sirve para poder administrar desde Django en caso de que queramos agregar datos de prueba
        return self.rut
        return self.nombre

import uuid as uuid
from django.db import models
from django.urls import reverse


# Create your models here.
class Director(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fechaNacimiento = models.DateField()
    fechaFallecimiento = models.DateField(null=True, blank=True)
    bio = models.TextField(max_length=2000)
    fotoLink = models.CharField(max_length=500, null=True)

    def get_absolute_url(self):
        return reverse('director_detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.nombre}, {self.apellido}'


class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)
    genero = models.ManyToManyField('Genero')
    anyoPub = models.IntegerField(help_text='Año de publicacion de la película')
    sinopsis = models.TextField(max_length=2000)
    fotoLink = models.CharField(max_length=500, null=True)

    def __str__(self):
        return f'{self.titulo}'
    def get_absolute_url(self):
        return reverse('pelicula_detail', args=[str(self.id)])


class Genero(models.Model):
    genero = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.genero}'

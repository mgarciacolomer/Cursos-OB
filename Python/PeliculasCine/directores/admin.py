from django.contrib import admin
from .models import Director, Pelicula, Genero

# Register your models here.
admin.site.register(Director)
admin.site.register(Pelicula)
admin.site.register(Genero)

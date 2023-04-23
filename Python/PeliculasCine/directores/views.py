from django.shortcuts import render
from django.views import generic
from .models import Director, Pelicula


# Create your views here.

class DirectorListView(generic.ListView):
    model = Director


class DirectorDetailView(generic.DetailView):
    model = Director

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["pelicula_list"] = Pelicula.objects.filter(director__id=kwargs['object'].id)
        context["id"] = kwargs['object'].id
        return context

class PeliculaDetailView(generic.DetailView):
    model = Pelicula

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["director"] = kwargs['object'].director
        context["generos"] = kwargs['object'].genero.all()
        return context

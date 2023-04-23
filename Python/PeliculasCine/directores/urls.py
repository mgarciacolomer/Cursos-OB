from django.shortcuts import redirect
from django.urls import re_path
from . import views

urlpatterns = [
    re_path('directores/', views.DirectorListView.as_view(), name='director_list'),
    re_path(r'^director/(?P<pk>\d+)$', views.DirectorDetailView.as_view(), name='director_detail'),
    re_path(r'^pelicula/(?P<pk>\d+)$', views.PeliculaDetailView.as_view(), name='pelicula_detail'),
]

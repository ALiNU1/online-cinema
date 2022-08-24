from django.shortcuts import render, redirect
from .models import Movie, Category, MovieShots
from apps.settings.models import Setting
from apps.movies.forms import MovieCreateForm,MovieUpdateForm
from django.db.models import Q
from django.http import HttpResponse

# Create your views here.
def movie_create(request):
    form = MovieCreateForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {
        'form': form,
    }
    return render(request, 'create.html', context)

def movie_details(request, id):
    movie = Movie.objects.get(id = id)
    setting= Setting.objects.latest('id')
    movie_shots = MovieShots.objects.all().filter(movie = movie)
    context={
        'movie': movie,
        'setting': setting, 
        'movie_shots': movie_shots,
    }
    return render(request, 'movie-details.html', context)

def movie_search(request):
    movies= Movie.objects.all()
    setting= Setting.objects.latest('id')
    qury_object= request.GET.get('key')
    if qury_object:
        posts = Movie.objects.filter(Q(title__icontains = qury_object) | Q(description__icontains = qury_object))
    context = {
        'setting' : setting,
        'movies' : movies
    }
    return render(request, 'search.html', context)


def movie_update(request, id):
    movie = Movie.objects.get(id = id)
    form = MovieUpdateForm(request.POST or None, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('movie_details', movie.id)
    context = {
        'form' : form,
    }
    return render(request, 'update.html', context)
from django.shortcuts import render, redirect
from .models import Movie, Category, MovieShots
from apps.settings.models import Setting
from apps.movies.forms import MovieCreateForm
from django.db.models import Q

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
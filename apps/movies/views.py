from django.shortcuts import render, redirect
from .models import Movie, Category
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
    context={
        'movie': movie,
        'setting': setting, 
    }
    return render(request, 'movie-details.html', context)
from django.shortcuts import render
from .models import Setting
from apps.movies.models import Movie
# Create your views here.


def index(request):
    setting = Setting.objects.latest('id')
    movie = Movie.objects.all().order_by('?')
    context = {
        'setting' : setting,
        'movie' : movie
    }
    return render(request, 'index.html', context)
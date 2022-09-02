from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import Movie, Category, MovieShots, Video
from apps.settings.models import Setting
from apps.movies.forms import MovieCreateForm,MovieUpdateForm
from django.db.models import Q
from django.http import StreamingHttpResponse
from .services import open_file

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
    film_video = Video.objects.get(movie=movie)
    context={
        'movie': movie,
        'setting': setting, 
        'movie_shots': movie_shots,
        "film_video":film_video
    }
    return render(request, 'movie-details.html', context)

def movie_search(request):
    movies = Movie.objects.all()
    qury_obj = request.GET.get('key')
    home = Setting.objects.latest('id')
    if qury_obj:
        movies = Movie.objects.filter(Q(title__icontains = qury_obj))
    context = {
        'home' : home, 
        'movies' : movies,
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

def movie_delete(request, id):
    context ={}
 
    obj = get_object_or_404(Movie, id = id)
    if request.method =="POST":

        obj.delete()
        return HttpResponseRedirect("/")
 
    return render(request, "delete.html", context)

def all_movies(request):
    all_movies = Movie.objects.all()
    setting = Setting.objects.latest('id')
    context = {
        'all_movies' : all_movies,
        'setting' : setting,
    }
    return render(request, "movie-grid.html", context )

# def get_list_video(request):
#     return render(request, 'index.html', {'video_list':Video.objects.all()})

# def get_video(request, pk:int):
#     _video = get_object_or_404(Video, id=pk)
#     return render(request, "video.html", {"video":_video})

# def get_streaming_video(request, pk: int):
#     file, status_code, content_length, content_range = open_file(request, pk)
#     response = StreamingHttpResponse(file, status=status_code, content_type='video/mp4')

#     response['Accept-Ranges'] = 'bytes'
#     response['Content-Length'] = str(content_length)
#     response['Cache-Control'] = 'no-cache'
#     response['Content-Range'] = content_range
#     return response

def video_watch(request,id):
    setting = Setting.objects.all()
    video  = Video.objects.get(id = id)
    context = {
        'setting' : setting,
        'video' : video,
    }
    return render(request, 'video.html', context)
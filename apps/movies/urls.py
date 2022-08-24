from unicodedata import name
from django.urls import path
from apps.movies.views import movie_create,  movie_details, movie_search, movie_update

urlpatterns = [
    path('create/', movie_create, name="create"),
    path('<int:id>', movie_details, name="movie_details"),
    path('search/', movie_search, name= "movie_search"),
    path('update/<int:id>', movie_update, name="movie_update"),
]
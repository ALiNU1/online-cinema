from django.urls import path
from apps.movies.views import (movie_create,  movie_details, movie_search, movie_update, movie_delete, 
all_movies, video_watch)

urlpatterns = [
    path('create/', movie_create, name="create"),
    path('<int:id>', movie_details, name="movie_details"),
    path('search/', movie_search, name= "movie_search"),
    path('update/<int:id>', movie_update, name="movie_update"),
    path('delete/<int:id>', movie_delete, name="movie_delete"),
    path('all-movies/', all_movies, name = "all_movies"),
    # path('stream/<int:pk>/', get_streaming_video, name='stream'),
    # path('<int:pk>/', get_video, name='video'), 
    # path('', get_list_video, name="get_list_video"),
    path('video/<int:id>/',video_watch, name= "video"),
]
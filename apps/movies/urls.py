from django.urls import path
from .views import movie_create

path('create/', movie_create, name="create"),
from django.urls import path
from .views import movie_create,  movie_details

urlpatterns = [
    path('create/', movie_create, name="create"),
    path('<int:id>', movie_details, name="movie_details")
]
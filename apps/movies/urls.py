from django.urls import path
from .views import movie_create, view_all

urlpatterns = [
    path('create/', movie_create, name="create"),
]
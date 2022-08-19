from django.shortcuts import render, redirect
from .models import Movie, Category
from apps.settings.models import Setting
from .forms import MovieCreateForm
from django.db.models import Q

# Create your views here.
def movie_create(request):
    form = MovieCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {
        'form': form,

    }
    return render(request, 'create.html', context)

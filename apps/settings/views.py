from django.shortcuts import render
<<<<<<< HEAD
from apps.settings.models import Setting
# Create your views here.


def index(request):
=======
from movies.models import Setting
# Create your views here.


def settings(request):
>>>>>>> fbad417bf1a3a52ae6033210a347b54d46757b2a
    setting = Setting.objects.latest('id')
    context = {
        'setting' : setting,
    }
    return render(request, 'index.html', context)
from django.shortcuts import render
from movies.models import Setting
# Create your views here.


def settings(request):
    setting = Setting.objects.latest('id')
    context = {
        'setting' : setting,
    }
    return render(request, 'index.html', context)
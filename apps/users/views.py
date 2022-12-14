from django.shortcuts import redirect, render
from apps.settings.models import Setting
from apps.users.models import User
from django.shortcuts import HttpResponse
from django.contrib.auth import login, authenticate

# Create your views here.
def register(request):
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
                user = User.objects.create(first_name = first_name, last_name = last_name,hone = phone, username = username,)
                user.set_password(password1)
                user.save()
                return redirect('index')

    context = {
        'setting' : setting,
    }
    return render(request, 'register.html', context)

def user_login(request):
    setting = Setting.objects.latest('id')
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = User.objects.get(username = username)
            user = authenticate(password = password)
        except:
            return HttpResponse("Неправильные данные")
    context = {
        'setting' : setting,
    }
    return render(request, 'login.html', context)    
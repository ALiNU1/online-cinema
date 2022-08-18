from django.shortcuts import redirect, render
from apps.settings.models import Setting
from apps.users.models import User
from django.shortcuts import HttpResponse
from django.contrib.auth import login, authenticate

# Create your views here.
def register(request):
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            try:
                user = User.objects.create(email = email)
                user.set_password(password1)
                user.save()
                return redirect('user_login')
            except:
                return HttpResponse("Неправильные данные")
        else:
            return HttpResponse("Пароли не совпадают")

    context = {
        'setting' : setting,
    }
    return render(request, 'sing-up.html', context)
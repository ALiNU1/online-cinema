from django.urls import path
from apps.users.views import register

urlpatterns = [
    path('sing-up/', register, name='register'),
]
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('', include('apps.settings.urls')),
    path('', include('apps.users.urls')),
=======
>>>>>>> fbad417bf1a3a52ae6033210a347b54d46757b2a
]

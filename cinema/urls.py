from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from apps.movies.views import movie_create
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.settings.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('apps.users.urls')),
    path('create/', movie_create, name="create"),
    path('logout/', LogoutView.as_view(next_page = 'index'), name="logout"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
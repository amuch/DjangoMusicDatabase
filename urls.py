from django.urls import path, include
from . import views

app_name = 'music'

urlpatterns = [
    path('', views.artists, name = 'artists'),
    path('api/', include('music.api.urls', namespace = 'api')),
    path('<slug:artist>/', views.artist, name = 'artist'),
    path('<slug:artist>/<slug:album>/', views.album, name = 'album'),
]
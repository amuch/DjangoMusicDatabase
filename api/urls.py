from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'music'

router = routers.DefaultRouter()
router.register(r'songs', views.SongViewSet)
router.register(r'artists', views.ArtistViewSet)
router.register(r'albums', views.AlbumViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
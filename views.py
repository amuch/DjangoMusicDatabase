from django.shortcuts import render, get_object_or_404
from .models import Artist, Album, Song

# List of all artists.
def artists(request):
    artists = Artist.objects.all().order_by('name')
    albums = Album.objects.all().order_by('artist', 'release')
    context = {'artists': artists, 'albums': albums}
    return render(request, 'music/artists.html', context)

# Individual artist.
def artist(request, artist):
    artist = get_object_or_404(Artist, slug = artist)
    songs = artist.songs.order_by('title', )
    context = {'artist': artist, 'songs': songs}
    return render(request, 'music/artist.html', context)

# Individual album.
def album(request, artist, album):
    album = get_object_or_404(Album, slug = album)
    songs = album.songs.order_by('track', 'title')
    context = {'album': album, 'songs': songs}
    return render(request, 'music/album.html', context)
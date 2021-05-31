from rest_framework import serializers
from ..models import Song, Artist, Album

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('name', )

class SongSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only = True)
    class Meta:
        model = Song
        fields = ('artist', 'track', 'title', 'song')

class AlbumSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many = True, read_only = True)
    artist = ArtistSerializer(read_only = True)
    class Meta:
        model = Album
        fields = ('artist', 'title', 'cover', 'release', 'songs')
from django.db import models
from django.urls import reverse
import datetime

class Artist(models.Model):
    name = models.CharField(max_length = 200)
    slug = models.SlugField(max_length = 200, unique = True)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('music:artist', args=[self.slug, ])

class Album(models.Model):
    title = models.CharField(max_length = 200)
    slug = models.SlugField(max_length = 200, unique = True)
    artist = models.ForeignKey(Artist, related_name = 'artists', on_delete = models.CASCADE)
    release = models.DateField(auto_now = False, auto_now_add = False, default = datetime.date(1900, 1, 1))
    folder = 'covers/'
    cover = models.ImageField(upload_to = folder, blank = True, null = True)

    class Meta:
        ordering = ('artist', 'release', 'title', )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('music:album', args=[self.artist.slug, self.slug, ])

class Song(models.Model):
    title = models.CharField(max_length = 200)
    artist = models.ForeignKey(Artist, related_name = 'songs', on_delete = models.CASCADE)
    album = models.ForeignKey(Album, related_name = 'songs', on_delete = models.CASCADE, blank = True, null = True)
    track = models.SmallIntegerField(default = 0)
    folder = 'music/'
    song = models.FileField(upload_to = folder)

    class Meta:
        ordering = ('artist', 'album', 'track', 'title', )

    def __str__(self):
        return self.title

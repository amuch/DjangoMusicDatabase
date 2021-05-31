from django.contrib import admin
from music.models import Artist, Album, Song

#admin.site.register(Artist)
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug')
	list_filter = ('name', )
	search_fields = ('name', )
	prepopulated_fields = {'slug': ('name', )}
	ordering = ('name', )

#admin.site.register(Album)
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'artist', 'release')
	list_filter = ('title', 'artist')
	search_fields = ('title', 'artist')
	prepopulated_fields = {'slug': ('title', )}
	ordering = ('artist', 'release', 'title')

#admin.site.register(Song)
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
	list_display = ('title', 'track', 'artist', 'album')
	list_filter = ('artist', 'album', 'title')
	search_fields = ('title', 'artist', 'album')
	ordering = ('artist', 'album', 'track', 'title')

from django.forms import model_to_dict
from rest_framework.viewsets import ModelViewSet

from albums.serializer import ArtistSerializer, TrackSerializer, AlbumSerializer

from albums.models import Artist, Track, Album


class ArtistListViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class TrackListViewSet(ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

    def get_queryset(self):
        filter = {}
        artist_name = self.request.query_params.get('artist_name', None)
        album_name = self.request.query_params.get('album_name', None)
        filter['artist__name'] = artist_name
        filter['album__name'] = album_name
        return Track.objects.filter(**filter)


class AlbumListViewSet(ModelViewSet):
    queryset = Album.objects.filter()
    serializer_class = AlbumSerializer

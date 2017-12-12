from rest_framework.viewsets import ModelViewSet

from albums.serializer import ArtistSerializer, TrackSerializer, AlbumSerializer

from albums.models import Artist, Track, Album


class ArtistListViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class TrackListViewSet(ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class AlbumListViewSet(ModelViewSet):
    queryset = Album.objects.filter()
    serializer_class = AlbumSerializer

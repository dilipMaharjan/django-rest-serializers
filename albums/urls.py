from rest_framework import routers

from albums.views import ArtistListViewSet, TrackListViewSet, AlbumListViewSet

router = routers.DefaultRouter()
router.register(r'artists', ArtistListViewSet)
router.register(r'tracks', TrackListViewSet)
router.register(r'albums', AlbumListViewSet)

urlpatterns = [
]

urlpatterns += router.urls

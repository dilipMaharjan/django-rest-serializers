from rest_framework import serializers

from albums.models import Album, Track, Artist


class AlbumSerializerWithStringRelatedField(serializers.ModelSerializer):
    tracks = serializers.StringRelatedField(many=True)

    class Meta:
        model = Album
        fields = ('album_name', 'artist', 'tracks')


class AlbumSerializerWithPrimaryKeyRelatedField(serializers.ModelSerializer):
    tracks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ('album_name', 'artist', 'tracks')


class AlbumSerializerHyperLinkedRelatedField(serializers.ModelSerializer):
    tracks = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='track-detail'
    )

    class Meta:
        model = Album
        fields = ('album_name', 'artist', 'tracks')


class AlbumSerializerWithSlugRelatedField(serializers.ModelSerializer):
    tracks = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )

    class Meta:
        model = Album
        fields = ('album_name', 'artist', 'tracks')


class AlbumSerializerWithHyperLinkedIdentityField(serializers.HyperlinkedModelSerializer):
    track_listing = serializers.HyperlinkedIdentityField(view_name='track-list')

    class Meta:
        model = Album
        fields = ('album_name', 'artist', 'track_listing')


class TrackSerializer(serializers.ModelSerializer):
    album = serializers.PrimaryKeyRelatedField(read_only=True)
    artist = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Track
        fields = ('order', 'title', 'duration', 'album', 'artist')


class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ('name', 'tracks')


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('name',)

from django.db import models


class Album(models.Model):
    album_name = models.CharField(max_length=100)

    def __str__(self):
        return self.album_name


class Artist(models.Model):
    name = models.CharField(max_length=100, default=1)

    def __str__(self):
        return self.name


class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, related_name='artist', on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        unique_together = ('album', 'order')
        ordering = ['order']

    def __unicode__(self):
        return '%d: %s' % (self.order, self.title)

    def __str__(self):
        return self.title

from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255, blank=True, null=True)
    genre = models.CharField(max_length=255)
    year = models.IntegerField(blank=True, null=True)
    lyrics = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='upload/%Y/%m/%d')
    audio_file = models.FileField(upload_to='upload/%Y/%m/%d')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
      return self.title

from django.db import models
# Create your models here.
from django.contrib.auth import get_user_model
from django.db import models
from embed_video.fields import EmbedVideoField
from django.utils import timezone
from django.urls import reverse

UserAuthor = get_user_model()

class MediaVideoModel(models.Model):
    user = models.ForeignKey(UserAuthor,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=255, blank=True)
    video_file = EmbedVideoField()
    slug = models.SlugField(max_length=200, db_index=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('resources:media',kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

class MediaImageModel(models.Model):
    user = models.ForeignKey(UserAuthor,on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    image_file = models.FileField(upload_to='documents/image/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('resources:media')
    # ,kwargs={'pk':self.pk})

    def __str__(self):
        return self.title


class MediaAudioModel(models.Model):
    user = models.ForeignKey(UserAuthor,on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    audio_file = models.FileField(upload_to='documents/audio/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('resources:media')
    # ,kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

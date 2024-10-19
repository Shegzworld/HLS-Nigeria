# (link unavailable)
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Podcaster(models.Model):
    name = models.CharField(max_length=255)

class Podcast(models.Model):
    title = models.CharField(max_length=255)
    podcaster = models.ForeignKey(Podcaster, on_delete = models.CASCADE, null = True)
    description = models.TextField()
    image = models.ImageField(upload_to='podcast_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    


class Episode(models.Model):
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE, related_name='episodes')
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='episode_images/', null = True)
    description = models.TextField()
    audio_file = models.FileField(upload_to='episode_audio/')
    duration = models.IntegerField(help_text='Duration in seconds')
    published_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.podcast.title} - {self.title}"


class Review(models.Model):
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[
    (1, '1 star'),
    (2, '2 stars'),
    (3, '3 stars'),
    (4, '4 stars'),
    (5, '5 stars'),
])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.podcast.title} - {self.user.username}"


class Subscription(models.Model):
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.podcast.title} - {self.user.username}"


class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    episodes = models.ManyToManyField(Episode)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.title}"

# Create your models here.


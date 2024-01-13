from django.db import models
from django.contrib.auth.models import User

class Mp3(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    mp3_file = models.FileField(upload_to='mp3s/', blank=True)
    # Add any additional fields you need for your MP3 model

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'

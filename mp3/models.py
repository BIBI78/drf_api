from django.db import models
from django.contrib.auth.models import User

class Mp3(models.Model):
    """
    Model for storing MP3 files uploaded by users.
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    mp3 = models.FileField(upload_to='mp3/', blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        """Returns a string representation of the Mp3 object."""
        return f'{self.id} {self.title}'

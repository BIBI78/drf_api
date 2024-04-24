from django.db import models
from django.contrib.auth.models import User

class Mp3(models.Model):
    """
    Model for storing MP3 files uploaded by users.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # User who uploaded the MP3
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the MP3 was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for when the MP3 was last updated
    title = models.CharField(max_length=255)  # Title of the MP3
    content = models.TextField(blank=True)  # Additional content related to the MP3
    mp3 = models.FileField(upload_to='mp3/', blank=True)  # FileField for storing the MP3 file

    class Meta:
        ordering = ['-created_at']  # Order MP3s by creation date in descending order

    def __str__(self):
        """
        Returns a string representation of the Mp3 object.
        """
        return f'{self.id} {self.title}'  # Concatenate ID and title for string representation

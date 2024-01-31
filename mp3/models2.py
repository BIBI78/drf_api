from django.db import models
from django.contrib.auth.models import User


class Mp3(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    # is this right ? im uploading it to the mp3 file in cloudinary 
    mp3 = models.FileField(upload_to='mp3/', blank=True) 


    # image = models.ImageField(
    #     upload_to='mp3/', default='../default_post_rgq6aq', blank=True
    # )
    # image_filter = models.CharField(
    #     max_length=32, choices=image_filter_choices, default='normal'
    # )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
from django.db import models
from django.contrib.auth.models import User


class Beat(models.Model):
    """
    BEAT BEAT model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
  
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    mp3 = models.FileField(upload_to='mp3/', blank=True) 
    # might be a problme witht default image 
    # might nedd to change the images to album covers?
    image = models.ImageField(
        upload_to='images/', default='../default_post_rgq6aq', blank=True, max_length=300
    )
   

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
from django.db import models
from django.contrib.auth.models import User
from mp3.models import Mp3  
from beats.models import Beat

class Like(models.Model):
    """
    Like model, related to 'owner','mp3'.
    'owner' is a User instance, 'mp3' is an Mp3 instance.
    'unique_together' makes sure a user can't like the same post or mp3 twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    mp3 = models.ForeignKey(
        Mp3, related_name='likes', on_delete=models.CASCADE, blank=True, null=True
    )
    beat = models.ForeignKey(
        Beat, related_name='likes', on_delete=models.CASCADE, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'mp3', 'beat']

    def __str__(self):
        return f'{self.owner} {self.mp3} {self.beat}'

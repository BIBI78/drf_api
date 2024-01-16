from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from mp3.models import Mp3  # Assuming you have an Mp3 model

class Like(models.Model):
    """
    Like model, related to 'owner', 'post', and 'mp3'.
    'owner' is a User instance, 'post' is a Post instance, and 'mp3' is an Mp3 instance.
    'unique_together' makes sure a user can't like the same post or mp3 twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='likes', on_delete=models.CASCADE, blank=True, null=True
    )
    mp3 = models.ForeignKey(
        Mp3, related_name='likes', on_delete=models.CASCADE, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post', 'mp3']

    def __str__(self):
        return f'{self.owner} {self.post} {self.mp3}'

from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Rating(models.Model):
    """ 
    Rating model with related name ratings
    """
    rating = models.IntegerField()
    # event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='ratings')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    #  new bs
    post = models.ForeignKey(
        Post, related_name='ratings', on_delete=models.CASCADE, blank=True, null=True
    )
   
   
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.owner} {self.event}'
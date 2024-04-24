from django.db import models
from django.contrib.auth.models import User

from beats.models import Beat


class Rating(models.Model):
    """ 
    Model to store ratings given by users to beats.
    """
    rating = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    beat = models.ForeignKey(
        Beat, related_name='ratings', on_delete=models.CASCADE, blank=True, null=True
    ) # Beat being rated

    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        """
        Returns a string representation of the Rating object.
        """
        return f'{self.owner} {self.beat}'
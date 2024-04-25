from django.db import models
from django.contrib.auth.models import User
from beats.models import Beat


class Comment(models.Model):
    """
    Comment model representing comments made by users on beats.
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    beat = models.ForeignKey(Beat, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']  # Order comments by creation date

    def __str__(self):
        """
        Returns a string representation of the Comment object.
        """
        return self.content  # Returns the content of the comment

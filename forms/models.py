from django.db import models
from django.contrib.auth.models import User

from beats.models import Beat


class Form(models.Model):
    """
    Forms model need to add something to this 
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
   
    # problem with the forein key
    beat = models.ForeignKey(Beat, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
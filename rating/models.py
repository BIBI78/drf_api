# rating/models.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg

class Rating(models.Model):
    """
    Rating model, related to User
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.owner.username} - {self.rating}'

    def average_rating(self):
        return Rating.objects.all().aggregate(Avg('rating'))['rating__avg']

from django.db import models
from django.contrib.auth.models import User
from beats.models import Beat

class Form(models.Model):
    CATEGORY_CHOICES = [
        ('fire', 'Fire'),
        ('cold', 'Cold'),
        ('banger', 'Banger'),
        ('snooze', 'Snooze'),
    ]

    title = models.CharField(max_length=100, default='')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Add this line
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    beat = models.ForeignKey(Beat, on_delete=models.CASCADE)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content

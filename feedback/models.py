from django.db import models
from django.contrib.auth.models import User
from beats.models import Beat

class Feedback(models.Model):
    owner = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='feedbacks',
        null=True,  
        blank=True,  
    )
    beat = models.ForeignKey(
        Beat, 
        on_delete=models.CASCADE,
        related_name='feedbacks',
        null=True,  
        blank=True,  
    )
    fire = models.BooleanField(default=False)
    cold = models.BooleanField(default=False)
    hard = models.BooleanField(default=False)
    trash = models.BooleanField(default=False)
    loop = models.BooleanField(default=False)
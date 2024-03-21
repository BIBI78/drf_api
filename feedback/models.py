from django.db import models
from django.contrib.auth.models import User
from beats.models import Beat

class FeedbackFire(models.Model):
    owner = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='feedbackfire',
        null=True,  
        blank=True,  
    )
    beat = models.ForeignKey(
        Beat, 
        on_delete=models.CASCADE,
        related_name='feedbackfire',
        null=True,  
        blank=True,  
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'beat']

    def __str__(self):
        return f'{self.owner}{self.beat}'

class FeedbackCold(models.Model):
    owner = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='feedbackcold',
        null=True,  
        blank=True,  
    )
    beat = models.ForeignKey(
        Beat, 
        on_delete=models.CASCADE,
        related_name='feedbackcold',
        null=True,  
        blank=True,  
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'beat']

    def __str__(self):
        return f'{self.owner}{self.beat}'

class FeedbackHard(models.Model):
    owner = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='feedbackhard',
        null=True,  
        blank=True,  
    )
    beat = models.ForeignKey(
        Beat, 
        on_delete=models.CASCADE,
        related_name='feedbackhard',
        null=True,  
        blank=True,  
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'beat']

    def __str__(self):
        return f'{self.owner}{self.beat}'

class FeedbackTrash(models.Model):
    owner = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='feedbacktrash',
        null=True,  
        blank=True,  
    )
    beat = models.ForeignKey(
        Beat, 
        on_delete=models.CASCADE,
        related_name='feedbacktrash',
        null=True,  
        blank=True,  
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'beat']

    def __str__(self):
        return f'{self.owner}{self.beat}'

class FeedbackLoop(models.Model):
    owner = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='feedbackloop',
        null=True,  
        blank=True,  
    )
    beat = models.ForeignKey(
        Beat, 
        on_delete=models.CASCADE,
        related_name='feedbackloop',
        null=True,  
        blank=True,  
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'beat']

    def __str__(self):
        return f'{self.owner}{self.beat}'

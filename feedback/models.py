from django.db import models
from django.contrib.auth.models import User
from beats.models import Beat


class FeedbackFire(models.Model):
    """
    Model representing feedback indicating a 'fire' reaction to a beat.
    """
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='feedbackfire',  # Related name for accessing feedback
        null=True,  # Allows the field to be null in the database
        blank=True,  # Allows the field to be blank in forms
    )
    beat = models.ForeignKey(
        Beat,
        on_delete=models.CASCADE,
        related_name='feedbackfire',  # Related name for accessing feedbackfire
        null=True,  # Allows the field to be null in the database
        blank=True,  # Allows the field to be blank in forms
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']  # Order feedback by creation date
        unique_together = ['owner', 'beat']  # Each user can give feedback

    def __str__(self):
        """
        Returns a string representation of the FeedbackFire object.
        """
        return f'{self.owner}{self.beat}'  # Concatenate owner and beat for rep


# more or less the same comments for other feedback models

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

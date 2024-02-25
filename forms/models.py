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
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    beat = models.ForeignKey(Beat, on_delete=models.CASCADE)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='')

    # def __str__(self):
    #     return self.title

# class FormSubmission(models.Model):
#     form = models.ForeignKey(Form, related_name='submissions', on_delete=models.CASCADE)
#     submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
#     submitted_at = models.DateTimeField(auto_now_add=True)
#     data = models.JSONField()

    class Meta:
        ordering = ['-created_at']

    # def __str__(self):
    #     return f"{self.form.title} Submission by {self.submitted_by.username}"

    def __str__(self):
        return self.content

from django.db import models
from django.contrib.auth.models import User
from categories.models import Category


class Interest(models.Model):
    """
    Interest model, related to 'owner', a user instance.
    Records profiles linked to a specific category
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=30, choices=Category.CATEGORIES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        # a user cannot choose the same category twice
        unique_together = ['owner', 'type']

    def __str__(self):
        return f"{self.type} {self.owner}"

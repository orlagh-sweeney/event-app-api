from django.db import models
from django.contrib.auth.models import User
from comments.models import Comment


class Like(models.Model):
    """
    Like model, related to 'owner' and 'comment'.
    'owner' is a User instance and 'comment' is a Comment instance.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(
        Comment, related_name='likes', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        # a user cannot like the same comment twice
        unique_together = ['owner', 'comment']

    def __str__(self):
        return f"{self.comment} {self.owner}"

from django.db import models
from django.contrib.auth.models import User
from events.models import Event


class Attendee(models.Model):
    """
    Attendee model, related to 'owner' and 'event'.
    'owner' is a User instance and 'event' is an Event instance.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, related_name='attendees', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        # a user cannot attend the same event twice
        unique_together = ['owner', 'event']

    def __str__(self):
        return f"{self.event} {self.owner}"

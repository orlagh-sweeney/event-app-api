from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    """
    Event model, related to 'owner', i.e. a User instance.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255, blank=False)
    date = models.DateField(blank=False)
    time = models.TimeField(blank=False)
    location = models.TextField(blank=False)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_event_image_senyfs',
        blank=True
    )
    # type = models.ForeignKey(
    #     Cateogry,
    #     on_delete=models.CASCADE,
    #     related_name="event_category"
    # )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'

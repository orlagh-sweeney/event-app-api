from rest_framework import generics, permissions
from .models import Event
from .serializers import EventSerializer
from drf_event_api.permissions import IsOwnerOrReadOnly


class EventList(generics.ListCreateAPIView):
    """
    List events or create an event if a user is logged in
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    # associate an event with a user upon creation
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve an event
    Update or delete an event if the user is the event owner
    """
    queryset = Event.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = EventSerializer

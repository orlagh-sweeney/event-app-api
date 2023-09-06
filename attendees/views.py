from rest_framework import generics, permissions
from drf_event_api.permissions import IsOwnerOrReadOnly
from .models import Attendee
from .serializers import AttendeeSerializer


class AttendeeList(generics.ListCreateAPIView):
    """
    List attendees or create an attendee if logged in
    """
    serializer_class = AttendeeSerializer
    # only authenticated users can attend an event
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Attendee.objects.all()

    # associate attendees with a user upon creation
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AttendeeDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve an attendee instance or delete it by id if you own it.
    """
    # only the user who chose to attened an event and can unattend
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = AttendeeSerializer
    queryset = Attendee.objects.all()

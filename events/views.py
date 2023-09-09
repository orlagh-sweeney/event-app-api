from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Event
from .serializers import EventSerializer
from drf_event_api.permissions import IsOwnerOrReadOnly


class EventList(generics.ListCreateAPIView):
    """
    List events or create an event if a user is logged in
    """
    queryset = Event.objects.annotate(
        # how many users are attending an event
        attending_count=Count('attendees', distinct=True),
        # how many comments on an event
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        # events a user is attending
        'attendees__owner__profile',
        # events a user has created
        'owner__profile',
        # filter events by type
        'type',
    ]
    search_fields = [
        'owner__username',
        'title',
    ]
    ordering_fields = [
        'attending_count',
        'comments_count',
        'attendees__created_at',
    ]
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
    queryset = Event.objects.annotate(
        # how many users are attending an event
        attending_count=Count('attendees', distinct=True),
        # how many comments on an event
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = EventSerializer

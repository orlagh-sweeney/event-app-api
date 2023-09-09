from django.db.models import Count
from rest_framework import generics, filters
from .models import Profile
from .serializers import ProfileSerializer
from drf_event_api.permissions import IsOwnerOrReadOnly, IsAuthenticatedOrIsOwner


class ProfileList(generics.ListAPIView):
    """
    List all profiles
    """
    queryset = Profile.objects.annotate(
        # how many events a user has created
        events_count=Count('owner__event', distinct=True),
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'events_count',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve a profile if authenticated
    Update a profile if you're the owner
    """
    queryset = Profile.objects.annotate(
        # how many events a user has created
        events_count=Count('owner__event', distinct=True),
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticatedOrIsOwner]

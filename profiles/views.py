from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer
from drf_event_api.permissions import IsOwnerOrReadOnly, IsAuthenticatedOrIsOwner


class ProfileList(generics.ListAPIView):
    """
    List all profiles
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve a profile if authenticated
    Update a profile if you're the owner
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticatedOrIsOwner]

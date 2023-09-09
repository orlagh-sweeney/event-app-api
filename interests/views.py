from rest_framework import generics, permissions
from drf_event_api.permissions import IsOwnerOrReadOnly
from .models import Interest
from .serializers import InterestSerializer


class InterestList(generics.ListCreateAPIView):
    """
    List interests or create an interest instance if logged in.
    """
    serializer_class = InterestSerializer
    # only authenticated users can create an interest instance
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Interest.objects.all()

    # associate interest with a user upon creation
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class InterestDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve an interest or delete it by id if you own it.
    """
    # only the user who created the interest instance can delete it
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = InterestSerializer
    queryset = Interest.objects.all()

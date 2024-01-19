from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Mp3
from .serializers import Mp3Serializer

class Mp3List(generics.ListCreateAPIView):
    """
    List MP3s or create an MP3 if logged in.
    The perform_create method associates the MP3 with the logged-in user.
    """
    serializer_class = Mp3Serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Mp3.objects.annotate(
        # Add any additional annotations you need for your MP3 model
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'owner__profile',
        # Add any additional fields you want to filter on
    ]
    search_fields = [
        'owner__username',
        'title',
        # Add any additional fields you want to search on
    ]
    ordering_fields = [
        # Add any additional fields you want to order on
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class Mp3Create(generics.CreateAPIView):
    """
    Create an MP3 if logged in.
    The perform_create method associates the MP3 with the logged-in user.
    """
    serializer_class = Mp3Serializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class Mp3Detail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve an MP3 and edit or delete it if you own it.
    """
    serializer_class = Mp3Serializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Mp3.objects.annotate(
        # Add any additional annotations you need for your MP3 model
    ).order_by('-created_at')

from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Rating
from .serializers import RatingSerializer

class RatingList(generics.ListCreateAPIView):
    """
    API endpoint to list ratings or create a new rating.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()

    def perform_create(self, serializer):
        """
        Method to perform creation of a new rating instance.
        """
        serializer.save(owner=self.request.user)


class RatingDetail(generics.RetrieveDestroyAPIView):
    """
    API endpoint to retrieve or delete a specific rating by its ID.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()
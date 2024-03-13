from rest_framework import generics, permissions
from .models import Feedback
from .serializers import FeedbackSerializer
from drf_api.permissions import IsOwnerOrReadOnly

class FeedbackCreateView(generics.ListCreateAPIView):
    """
    Create feedback instances.

    Only authenticated users can create feedback.
    """
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class FeedbackUpdateView(generics.UpdateAPIView):
    """
    Update feedback instances.

    Only authenticated users can update feedback.
    """
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.IsAuthenticated]

class FeedbackListView(generics.ListAPIView):
    """
    Retrieve a list of feedback instances.

    Allows all users to view feedback.
    """
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.AllowAny]  # Allow any user to view feedback

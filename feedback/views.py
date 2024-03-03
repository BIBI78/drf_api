from rest_framework import generics, permissions
from .models import Feedback
from .serializers import FeedbackSerializer

class FeedbackCreateView(generics.CreateAPIView):
    """
    Create feedback instances.

    Only authenticated users can create feedback.
    """
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.IsAuthenticated]

class FeedbackUpdateView(generics.UpdateAPIView):
    """
    Update feedback instances.

    Only authenticated users can update feedback.
    """
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.IsAuthenticated]

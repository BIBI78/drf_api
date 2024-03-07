from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
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



 

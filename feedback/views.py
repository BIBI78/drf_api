from rest_framework import generics, permissions
from .models import Feedback
from .serializers import FeedbackSerializer
from drf_api.permissions import IsOwnerOrReadOnly
from django.http import JsonResponse
from beats.models import Beat 

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

def get_feedback_counts(request, beat_id):
    try:
        beat = Beat.objects.get(pk=beat_id)
        feedback_counts = {
            'fire': beat.feedback_set.filter(fire=True).count(),
            'cold': beat.feedback_set.filter(cold=True).count(),
            'hard': beat.feedback_set.filter(hard=True).count(),
            'trash': beat.feedback_set.filter(trash=True).count(),
            'loop': beat.feedback_set.filter(loop=True).count(),
        }

        # Update the feedback counts in the Beat object
        beat.fire_count = feedback_counts['fire']
        beat.cold_count = feedback_counts['cold']
        beat.hard_count = feedback_counts['hard']
        beat.trash_count = feedback_counts['trash']
        beat.loop_count = feedback_counts['loop']
        beat.save()

        return JsonResponse(feedback_counts)
    except Beat.DoesNotExist:
        return JsonResponse({'error': 'Beat not found'}, status=404)
from django.db.models import Count, Case, When, BooleanField
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Beat
from .serializers import BeatSerializer
from feedback.models import Feedback  # Assuming the feedback app name is 'feedback'

class BeatList(generics.ListCreateAPIView):
    """
    List the beats etc etc etc
    """
    serializer_class = BeatSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Beat.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True),
        fire_count=Count(Case(When(feedbacks__fire=True, then=1), output_field=BooleanField())),
        cold_count=Count(Case(When(feedbacks__cold=True, then=1), output_field=BooleanField())),
        hard_count=Count(Case(When(feedbacks__hard=True, then=1), output_field=BooleanField())),
        trash_count=Count(Case(When(feedbacks__trash=True, then=1), output_field=BooleanField())),
        loop_count=Count(Case(When(feedbacks__loop=True, then=1), output_field=BooleanField())),
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',  
        'likes__owner__profile',
        'owner__profile',
    ]
    search_fields = [
        'owner__username',
        'title',
    ]
    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BeatDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a BEAT and edit or delete it if you own it.
    """
    serializer_class = BeatSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Beat.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)  
    ).order_by('-created_at')

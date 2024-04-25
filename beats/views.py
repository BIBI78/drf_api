from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Beat
from .serializers import BeatSerializer
from feedback.models import (
    FeedbackFire,
    FeedbackCold,
    FeedbackHard,
    FeedbackTrash,
    FeedbackLoop,
)


class BeatList(generics.ListCreateAPIView):
    """
    API endpoint for listing and creating beats.
    """
    serializer_class = BeatSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Beat.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True),
        fire_count=Count('feedbackfire', distinct=True),
        cold_count=Count('feedbackcold', distinct=True),
        hard_count=Count('feedbackhard', distinct=True),
        trash_count=Count('feedbacktrash', distinct=True),
        loop_count=Count('feedbackloop', distinct=True),
    )
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
        """
        Perform creation of a new beat.
        """
        serializer.save(owner=self.request.user)


class BeatDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for retrieving, updating, and deleting a beat.
    """
    serializer_class = BeatSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Beat.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True),
        fire_count=Count('feedbackfire', distinct=True),
        cold_count=Count('feedbackcold', distinct=True),
        hard_count=Count('feedbackhard', distinct=True),
        trash_count=Count('feedbacktrash', distinct=True),
        loop_count=Count('feedbackloop', distinct=True),
    ).order_by('-created_at')

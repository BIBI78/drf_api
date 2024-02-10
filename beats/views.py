from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Beat
from .serializers import BeatSerializer


class BeatList(generics.ListCreateAPIView):
    """
    List the beats etc etc etc
    """
    serializer_class = BeatSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Beat.objects.annotate(
        # likes_count=Count('likes', distinct=True),
        # comments_count=Count('comments', distinct=True)  # Corrected related name
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        # 'owner__profile__followed__owner__profile',  # Corrected field name
        # 'likes__owner__profile',
        # 'owner__profile',
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
        # likes_count=Count('likes', distinct=True),
        # comments_count=Count('comments', distinct=True)  # Corrected related name
    ).order_by('-created_at')

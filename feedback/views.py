
from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Beat

from rest_framework.response import Response
from .models import FeedbackFire
from .serializers import FeedbackFireSerializer

from rest_framework import generics, permissions
from .models import FeedbackFire, FeedbackCold, FeedbackHard, FeedbackTrash, FeedbackLoop
from .serializers import (
    FeedbackFireSerializer, FeedbackColdSerializer,
    FeedbackHardSerializer, FeedbackTrashSerializer, FeedbackLoopSerializer
)
from drf_api.permissions import IsOwnerOrReadOnly

class FeedbackFireList(generics.ListCreateAPIView):
    """
    List feedbacks or create a new feedback for fire.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FeedbackFireSerializer
    queryset = FeedbackFire.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class FeedbackColdList(generics.ListCreateAPIView):
    """
    List feedbacks or create a new feedback for cold.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FeedbackColdSerializer
    queryset = FeedbackCold.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class FeedbackHardList(generics.ListCreateAPIView):
    """
    List feedbacks or create a new feedback for hard.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FeedbackHardSerializer
    queryset = FeedbackHard.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class FeedbackTrashList(generics.ListCreateAPIView):
    """
    List feedbacks or create a new feedback for trash.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FeedbackTrashSerializer
    queryset = FeedbackTrash.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class FeedbackLoopList(generics.ListCreateAPIView):
    """
    List feedbacks or create a new feedback for loop.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FeedbackLoopSerializer
    queryset = FeedbackLoop.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # DETAIL

class FeedbackFireDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a like or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FeedbackFireSerializer
    queryset = FeedbackFire.objects.all()

class FeedbackColdDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a like or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FeedbackColdSerializer
    queryset = FeedbackCold.objects.all()

class FeedbackHardDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a like or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FeedbackHardSerializer
    queryset = FeedbackHard.objects.all()

class FeedbackTrashDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a like or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FeedbackTrashSerializer
    queryset = FeedbackTrash.objects.all()

class FeedbackLoopDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a like or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FeedbackLoopSerializer
    queryset = FeedbackLoop.objects.all()



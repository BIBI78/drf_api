from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Form
from .serializers import FormSerializer, FormDetailSerializer


class FormList(generics.ListCreateAPIView):
    """
    List comments or create a comment if logged in.
    """
    serializer_class = FormSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Form.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['beat']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FormDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a comment, or update or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FormDetailSerializer
    queryset = Form.objects.all()

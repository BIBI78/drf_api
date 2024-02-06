from django.urls import path
from mp3.views import Mp3List, Mp3Detail, Mp3Create

urlpatterns = [
    path('mp3s/', Mp3List.as_view(), name='mp3-list'),
    path('mp3s/create/', Mp3Create.as_view(), name='mp3-create'),  # Added for Mp3Create
    path('mp3s/<int:pk>/', Mp3Detail.as_view(), name='mp3-detail'),
    
]
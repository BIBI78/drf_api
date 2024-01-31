from django.urls import path
from mp3s import views

urlpatterns = [
    path('mp3s/', views.Mp3List.as_view()),
    path('mp3s/<int:pk>/', views.Mp3Detail.as_view())
]
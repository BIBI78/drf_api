from django.urls import path
from mp3 import views

urlpatterns = [
    path('mp3/', views.Mp3List.as_view()),
    path('mp3/<int:pk>/', views.Mp3Detail.as_view())
]
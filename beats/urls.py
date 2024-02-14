from django.urls import path
from beats import views

urlpatterns = [
    path('beats/', views.BeatList.as_view()),
    path('beats/<int:pk>/', views.BeatDetail.as_view())
   
]
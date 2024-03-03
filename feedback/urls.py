from django.urls import path
from feedback import views

urlpatterns = [
    path('feedback/', views.FeedbackCreateView.as_view(), name='feedback-create'),
    path('feedback/<int:pk>/', views.FeedbackUpdateView.as_view(), name='feedback-update'),
]


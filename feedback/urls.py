from django.urls import path
from feedback import views


urlpatterns = [
    path('feedback/fire/', views.FeedbackFireList.as_view(), name='feedback-fire-list'),
    path('feedback/fire/<int:pk>/', views.FeedbackFireDetail.as_view(), name='feedback-fire-detail'),

    path('feedback/cold/', views.FeedbackColdList.as_view(), name='feedback-cold-list'),
    path('feedback/cold/<int:pk>/', views.FeedbackColdDetail.as_view(), name='feedback-cold-detail'),

    path('feedback/hard/', views.FeedbackHardList.as_view(), name='feedback-hard-list'),
    path('feedback/hard/<int:pk>/', views.FeedbackHardDetail.as_view(), name='feedback-hard-detail'),

    path('feedback/trash/', views.FeedbackTrashList.as_view(), name='feedback-trash-list'),
    path('feedback/trash/<int:pk>/', views.FeedbackTrashDetail.as_view(), name='feedback-trash-detail'),

    path('feedback/loop/', views.FeedbackLoopList.as_view(), name='feedback-loop-list'),
    path('feedback/loop/<int:pk>/', views.FeedbackLoopDetail.as_view(), name='feedback-loop-detail'),
]

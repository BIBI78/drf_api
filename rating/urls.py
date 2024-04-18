from django.urls import path
from rating import views

urlpatterns = [
    path('rating/', views.RatingList.as_view()),
    path('rating/<int:pk>/', views.RatingDetail.as_view()),
]
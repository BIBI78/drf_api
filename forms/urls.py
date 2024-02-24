from django.urls import path
from forms import views

# does this make sense? 
urlpatterns = [
    path('forms/', views.FormList.as_view()),
    path('forms/<int:pk>/', views.FormDetail.as_view())
]
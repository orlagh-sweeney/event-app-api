from django.urls import path
from interests import views

urlpatterns = [
    path('interests/', views.InterestList.as_view()),
    path('interests/<int:pk>/', views.InterestDetail.as_view()),
]

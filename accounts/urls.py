from . import views
from django.urls import path

urlpatterns = [
    path('register/', views.RegisterUserAPIView.as_view()),

]
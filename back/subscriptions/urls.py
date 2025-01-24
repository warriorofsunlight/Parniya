from django.urls import path
from .views import (PlanView, SubscribeView)

urlpatterns = [
    path('plans/', PlanView.as_view()),
    path('sub/', SubscribeView.as_view()),
]
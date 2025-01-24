from django.urls import path
from .views import ColabView

urlpatterns = [
      path('colab-register/', ColabView.as_view()),
]
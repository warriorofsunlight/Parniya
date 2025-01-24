from django.urls import path
from .views import (RegisterUserView, LoginUserView,
                    OTPView, VerifyOTPView)

urlpatterns = [
    path('register/', RegisterUserView.as_view()),
    path('login/', LoginUserView.as_view()),
    path('generate-otp/', OTPView.as_view()),
    path('verify-otp/', VerifyOTPView.as_view()),   
]
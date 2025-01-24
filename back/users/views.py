from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.core.cache import cache

import random

from .serializers import UserSerializer

class OTPView(APIView):
    def post(self, request):
        otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        email = request.data.get('email')
        cache_key = f'otp_{email}'

        cache.set(cache_key, otp, timeout=300)
        return Response({'otp': otp},
                         status=status.HTTP_201_CREATED)
    
class VerifyOTPView(APIView):
    def post(self, request):
        email = request.data.get('email')
        user_otp = request.data.get('otp')
        cache_key = f'otp_{email}'
        cached_otp = cache.get(cache_key)

        if user_otp == cached_otp:
            return Response({'message': True},
                             status=status.HTTP_200_OK)
        return Response({'message': False},
                         status=status.HTTP_400_BAD_REQUEST)

class RegisterUserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data,
                                status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors,
                         status=status.HTTP_400_BAD_REQUEST)
    
class LoginUserView(APIView):
    def post(self, request):
        phone_number = request.data.get('email')
        password = request.data.get('password')

        if not phone_number or not password:
            return Response({'message': 'Enter both email and password'},
                            status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(email=phone_number, password=password)

        if not user:
            return Response({'message': 'phone number or password is not valid'},
                            status=status.HTTP_404_NOT_FOUND)
        
        refresh = RefreshToken.for_user(user)
        return Response({'refresh':str(refresh),  
                        'access': str(refresh.access_token),
                        'username': user.email.split('@')[0],
                        },
                        status=status.HTTP_200_OK)
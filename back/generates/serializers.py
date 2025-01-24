from rest_framework import serializers
from .models import Image
from users.serializers import UserSerializer

class ImageSerializer(serializers.ModelSerializer):
    user = UserSerializer

    class Meta:
        model = Image
        fields = '__all__'
        read_only_fields = ['user', 'created_at']
    
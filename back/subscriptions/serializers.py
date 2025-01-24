from rest_framework import serializers
from .models import Plans, Subscribes
from users.serializers import UserSerializer

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plans
        fields = '__all__'


class SubscribeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    plan = PlanSerializer()
    
    class Meta:
        model = Subscribes
        fields = '__all__'
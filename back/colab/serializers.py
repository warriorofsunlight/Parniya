from rest_framework import serializers
from .models import Colab

class ColabSerializer(serializers.ModelSerializer):

    class Meta:
        model = Colab
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'name':{'write_only':True},
            'last_name':{'write_only':True},
            'email':{'write_only':True},
            'linkedin':{'write_only':True},
            'cv':{'write_only':True},
        }
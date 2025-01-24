from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.core.files.base import ContentFile

from generator import generate

from io import BytesIO
import time

from subscriptions.models import Subscribes
from.models import Image
from .serializers import ImageSerializer
from .permissions import SubPermission

class ImageGenerateView(APIView):
    permission_classes = [IsAuthenticated, SubPermission]
    
    def post(self, request):
        prompt = request.data.get('prompt', None)

        if prompt:
            image = generate(prompt)

            with BytesIO() as buffer:
                image.save(buffer, format='JPEG')
                image_data = buffer.getvalue()

            image_record = Image.objects.create(user=request.user,
                                                prompt=prompt,
                                                )
            image_record.image.save(f'{int(time.time())}.jpg', ContentFile(image_data))
            image_record.save()
            subscribe = Subscribes.objects.get(user=request.user)
            subscribe.remain_images -= 1
            subscribe.save()
            serializer = ImageSerializer(image_record)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response({'message': 'Prompt is required'},
                         status=status.HTTP_400_BAD_REQUEST)
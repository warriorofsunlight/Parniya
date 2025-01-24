from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from generates.models import Image
from .serializers import ImageSerializer

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        try:
            images = Image.objects.filter(user=user)
        except Image.DoesNotExist:
            return Response({'message': 'You have no image yet'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ImageSerializer(images, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    

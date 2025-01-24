from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

import datetime

from .models import Plans, Subscribes
from .serializers import PlanSerializer, SubscribeSerializer

class PlanView(APIView):
    def get(self, request):
        plans = Plans.objects.all()

        serializer = PlanSerializer(plans, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
class SubscribeView(APIView):
    
    permission_classes = [IsAuthenticated]

    def post(self, request):
        plan_id = request.data.get('plan_id', None)
        if plan_id:
            plan = Plans.objects.get(id=plan_id)
            try:
                subscribe = Subscribes.objects.get(user=request.user)
            except Subscribes.DoesNotExist:
                subscribe = None
            if subscribe:
                subscribe.plan = plan
                subscribe.exp_date = datetime.datetime.now()+datetime.timedelta(days=plan.duration*30)
                subscribe.remain_images = plan.image_limit_per
                subscribe.save()
                serializer = SubscribeSerializer(data=subscribe)
                if serializer.is_valid():
                    serializer.save()
            else:
                subscribe = Subscribes.objects.create(user=request.user,
                                                      plan=plan,
                                                      exp_date = datetime.datetime.now()+datetime.timedelta(days=plan.duration*30),
                                                      remain_images=plan.image_limit_per)
                serializer = SubscribeSerializer(data=subscribe)
                if serializer.is_valid():
                    serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'message': 'You should select a plan'}, status=status.HTTP_400_BAD_REQUEST)
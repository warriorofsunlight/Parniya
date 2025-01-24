from rest_framework.permissions import BasePermission
from subscriptions.models import Subscribes
from django.utils import timezone

class SubPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        subscribe = Subscribes.objects.get(user=user)
        if subscribe.exp_date >= timezone.now():
            if subscribe.remain_images > 0:
                return True
        return False
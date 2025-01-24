from django.db import models

from users.models import User

class Plans(models.Model):
    title = models.CharField(max_length=64)
    duration = models.PositiveSmallIntegerField()
    image_limit_per = models.PositiveIntegerField(null=True, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.title} for {self.duration}'

class Subscribes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plans, on_delete=models.CASCADE)
    remain_images = models.PositiveIntegerField(blank=True, null=True)
    exp_date = models.DateTimeField()

    def __str__(self) -> str:
        return f'{self.user} until {self.exp_date}'
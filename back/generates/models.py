from django.db import models
from users.models import User

class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prompt = models.TextField(max_length=1024)
    image = models.ImageField(upload_to='media/generated_images')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.user} Wanted {self.prompt[:50]}'
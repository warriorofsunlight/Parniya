from django.db import models

class Colab(models.Model):
    name = models.CharField(max_length=11)
    last_name = models.CharField(max_length=11)
    email = models.EmailField(unique=True)
    cv = models.FileField(upload_to='cv/', null=True)
    linkedin = models.CharField(max_length=512)

    def __str__(self) -> str:
        return f'{self.email} : {self.linkedin}'
    
    
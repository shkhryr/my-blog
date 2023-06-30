from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(default='default.svg', upload_to='profile')

    def __str__(self):
        return f'{self.username}\'s profile'

    def save(self, **kwargs):
        super().save(**kwargs)


from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=10)
    address = models.TextField()
    profile_picture = models.ImageField(null=True, blank=True, upload_to='user_profile')

    def __str__(self):
        return str(self.user)
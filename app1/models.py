from django.db import models
from django.contrib.auth.models import User

#Django Models here

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_setting_1 = models.BooleanField(default=False)

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class CustomUser(AbstractUser):
    display_name = models.CharField(max_length=50, null=True)
    following = models.ManyToManyField('self', symmetrical=False, blank=True, related_name="followers")
    REQUIRED_FIELDS = ['display_name']

    def __str__(self):
        return self.username


from django.db import models
from twitteruser.models import CustomUser
from tweet.models import Tweet
from django.utils.timezone import now


class Notification(models.Model):
    at_person = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    the_tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    CHOICES = ((True, True), (False, False))
    read = models.BooleanField(choices=CHOICES, default=False)

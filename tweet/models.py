
from django.db import models
from django.utils.timezone import now
from django.urls import reverse
from twitteruser.models import CustomUser


class Tweet(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    tweet = models.TextField()
    timestamp = models.DateTimeField(default=now, editable=False)
    
    def get_absolute_url(self):
        return reverse('tweet-detail', kwargs={'pk': self.pk})

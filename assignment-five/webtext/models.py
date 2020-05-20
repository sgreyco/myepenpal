import datetime
from django.db import models
from django.utils import timezone


class User(models.Model):
    username = models.CharField(max_length=30)

    def __str__(self):
        return self.username


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender') # this is the sender
    recipient = models.ForeignKey(User, default=1, on_delete=models.CASCADE, related_name='recipient')
    message_text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date sent')

    def __str__(self):

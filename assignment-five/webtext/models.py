import datetime

from django.db import models


class User(models.Model):
    username = models.CharField(max_length=30)
    # register_date = models.DateTimeField('date registered')

    # messages_sent: a list of messages sent by the user, by Message id
    # messages_received: a list of messages received by the user, by Message id

    def __str__(self):
        return self.username


class Message(models.Model):
    sender = models.ForeignKey(User, default='sender', on_delete=models.SET_DEFAULT, related_name='author')
    # receiver = models.ForeignKey(User, default='receiver', on_delete=models.SET_DEFAULT, related_name='recipient')
    message_text = models.CharField(max_length=1000)

    def __str__(self):
        return self.message_text

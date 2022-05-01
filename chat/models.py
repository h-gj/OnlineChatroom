from django.db import models


class Message(models.Model):
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    room_name = models.CharField(max_length=16)

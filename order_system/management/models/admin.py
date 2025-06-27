from django.db import models


class BroadcastMessage(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    sent = models.BooleanField(default=False)

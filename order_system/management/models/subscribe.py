from django.db import models


class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()


class UserSubscription(models.Model):
    user_id = models.BigIntegerField(unique=True)
    is_subscribed = models.BooleanField(default=False)

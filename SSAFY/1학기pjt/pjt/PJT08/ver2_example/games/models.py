from django.db import models


class GameSession(models.Model):
    target_number = models.IntegerField()
    user_guess = models.IntegerField(null=True, blank=True)
    attempts = models.IntegerField(default=0)

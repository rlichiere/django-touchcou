
from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):

    name = models.CharField(max_length=200)
    players = models.ManyToManyField(User)

    def __str__(self):
        return self.name

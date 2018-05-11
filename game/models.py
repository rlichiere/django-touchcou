
from django.db import models
from django.contrib.auth.models import User

from .core.constants import GAME_STATUS, GAME_GENRES


class Game(models.Model):

    name = models.CharField(max_length=200)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    players = models.ManyToManyField(User, related_name='games')
    status = models.CharField(max_length=200, choices=GAME_STATUS.as_choices(), default=GAME_STATUS.default)
    genre = models.CharField(max_length=2, choices=GAME_GENRES.as_choices(), default=GAME_GENRES.default)

    def __str__(self):
        return self.name

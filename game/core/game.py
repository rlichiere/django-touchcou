
from game import models


class GameLogic(object):

    def __init__(self):
        pass

    def createGame(self, game_name, game_genre, game_creator):
        _game = models.Game(name=game_name, genre=game_genre, creator=game_creator)
        _game.save()
        return _game

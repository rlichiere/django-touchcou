
from abc import abstractmethod


class ConstantsGeneric(object):

    @abstractmethod
    def default(self):
        """ must return the default key """
        return str()

    @abstractmethod
    def as_list(self):
        """ must return the list of constants keys """
        return list()

    def as_list_labels(self):
        return ', '.join([_ for _ in self.as_list()])

    def as_choices(self):
        _res = list()
        for choice in self.as_list():
            _res.append(tuple((choice, choice)))
        return _res

    def keys_alphabet(self):
        _alphabet = ''
        for _key in self.as_list():
            for _c in _key:
                if not _alphabet.find(_c):
                    _alphabet += _c
        return _alphabet

    def length_of_longer_key(self):
        _max = 0
        for _genre in self.as_list():
            _max = max(_max, len(_genre))
        return _max


class GameStatusConstants(ConstantsGeneric):
    WAITING_REGISTRATIONS_OPENING = 'WAITING_REGISTRATIONS_OPENING'
    WAITING_PLAYERS = 'WAITING_PLAYERS'
    WAITING_GAME_LAUNCH = 'WAITING_GAME_LAUNCH'
    WAITING_PLAYER_INPUT = 'WAITING_PLAYER_INPUT'
    PROCESSING_PLAYER_INPUT = 'PROCESSING_PLAYER_INPUT'
    PLAYER_WINS = 'PLAYER_WINS'
    FINISHED = 'FINISHED'

    @property
    def default(self):
        return self.WAITING_REGISTRATIONS_OPENING

    def as_list(self):
        return [
            self.WAITING_REGISTRATIONS_OPENING,
            self.WAITING_PLAYERS,
            self.WAITING_GAME_LAUNCH,
            self.WAITING_PLAYER_INPUT,
            self.PROCESSING_PLAYER_INPUT,
            self.PLAYER_WINS,
            self.FINISHED,
        ]

    def getNext(self, status):
        if status == self.WAITING_REGISTRATIONS_OPENING:
            return self.WAITING_PLAYERS

        if status == self.WAITING_PLAYERS:
            return self.WAITING_GAME_LAUNCH

        if status == self.WAITING_GAME_LAUNCH:
            return self.WAITING_PLAYER_INPUT

        if status == self.WAITING_PLAYER_INPUT:
            return self.PROCESSING_PLAYER_INPUT

        if status == self.PROCESSING_PLAYER_INPUT:
            return self.PLAYER_WINS

        if status == self.PLAYER_WINS:
            return self.FINISHED

        if status == self.FINISHED:
            return self.FINISHED
        else:
            return self.WAITING_REGISTRATIONS_OPENING


class GameGenreConstants(ConstantsGeneric):
    HF = 'HF'
    FH = 'FH'
    HH = 'HH'
    FF = 'FF'

    @property
    def default(self):
        return self.HF

    def as_list(self):
        return [
            self.HF,
            self.FH,
            self.HH,
            self.FF,
        ]


GAME_STATUS = GameStatusConstants()
GAME_GENRES = GameGenreConstants()

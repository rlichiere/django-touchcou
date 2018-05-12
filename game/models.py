
import json

from django.db import models
from django.contrib.auth.models import User

from utils import utils
from .core.constants import GAME_STATUS, GAME_GENRES


class Game(models.Model):
    name = models.CharField(max_length=200)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=200, choices=GAME_STATUS.as_choices(), default=GAME_STATUS.default)
    genre = models.CharField(max_length=GAME_GENRES.max_length(),
                             choices=GAME_GENRES.as_choices(),
                             default=GAME_GENRES.default)

    def __str__(self):
        return self.name

    def registrationsOpened(self):
        if self.participations.count() < len(self.genre):
            return True
        return False


def createGame(game_name, game_genre, game_creator):
    _game = Game(name=game_name, genre=game_genre, creator=game_creator)
    _game.save()
    return _game


class JsonField(models.TextField):

    def __init__(self, *args, **kwargs):
        kwargs['default'] = '{"touchables": []}'
        super(JsonField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs['default']
        return name, path, args, kwargs

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value

        return json.loads(value)

    def to_python(self, value):
        if isinstance(value, dict):
            return value

        if value is None:
            return value

        return json.loads(str(value).replace("'", '"'))

    def get_prep_value(self, value):
        return json.dumps(value, separators=(',', ':'))

    def get_db_prep_value(self, value, connection, prepared=False):
        value = super().get_db_prep_value(value, connection, prepared)
        if value is not None:
            return str(value)
        return value


class JsonFieldWrapper(object):
    _modelObject = object
    _modelField = str

    def __init__(self, model_object, json_field):
        self._modelObject = model_object
        self._modelField = json_field

    def get(self, path=None):
        _data = getattr(self._modelObject, self._modelField)
        return utils.access(_data, path)

    def set(self, path, value):
        _data = getattr(self._modelObject, self._modelField)
        utils.access(_data, path, value)
        getattr(self._modelObject, 'save')()


class PlayerPreparationFieldWrapper(JsonFieldWrapper):

    def __init__(self, *args, **kwargs):
        super(PlayerPreparationFieldWrapper, self).__init__(*args, **kwargs)

    def setTouchable(self, media, zone):
        _mediaData = self.get('touchables/%s' % media)
        if type(_mediaData) is list:
            _mediaData.append(zone)
        else:
            _mediaData = [zone]

        self.set('touchables/%s' % media, _mediaData)

    def removeTouchable(self, media, zone):
        _touchablesData = self.get('touchables')
        _mediaData = _touchablesData.get(media)
        if type(_mediaData) is list:

            # remove zone from media
            _mediaData.remove(zone)
            _touchablesData[media] = _mediaData

            # remove media if became empty
            if len(_mediaData) < 1:
                _touchablesData.pop(media)

            # store data
            self.set('touchables', _touchablesData)

        else:
            _msg = 'Should not pass here, because we would never remove a unexisting touchable'
            print(_msg)
            raise Exception(_msg)

    def getMediasList(self):
        _res = list()
        for _mediaConf in self.get('touchables'):
            _res.append(_mediaConf)
        return _res

    def getZonesList(self):
        _res = list()
        for _mediaConfKey, _mediaConfValue in self.get('touchables').items():
            for _zoneKey in _mediaConfValue:
                if _zoneKey not in _res:
                    _res.append(_zoneKey)
        return _res


class UserParticipation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='participations')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='participations')
    player_genre = models.CharField(max_length=GAME_GENRES.max_length(), choices=GAME_GENRES.keys_alphabet())
    _preparation = JsonField()
    preparation = None

    def __init__(self, *args, **kwargs):
        super(UserParticipation, self).__init__(*args, **kwargs)
        self.preparation = PlayerPreparationFieldWrapper(model_object=self, json_field='_preparation')

    def __str__(self):
        return str(self.id)

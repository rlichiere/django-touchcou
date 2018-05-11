
from django import forms
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from .core import game
from .core.constants import GAME_GENRES


class CreateGameForm(forms.Form):
    name = forms.CharField(label='Game name', help_text='Give a name to your game')
    genre = forms.CharField(label='Game genre', help_text='Select a game genre : %s' % GAME_GENRES.as_list_labels())
    creator = forms.CharField(label='Game creator', help_text='Select a player name', required=False)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')

        super(CreateGameForm, self).__init__(*args, **kwargs)

        self.fields['genre'].initial = GAME_GENRES.default
        # self.fields['genre'].help_text = 'Select a game genre : %s' % GAME_GENRES.as_list_labels()

        if self.request.user.is_anonymous:
            self.fields['creator'].required = True
        else:
            self.fields['creator'].widget = forms.HiddenInput()

        self.game = None

    def execute(self):
        try:
            # retrieve form fields
            _gameName = self.cleaned_data['name']

            _gameGenre = self.cleaned_data['genre']
            if _gameGenre not in GAME_GENRES.as_list():
                return False, 'Game genre unknown : %s' % _gameGenre

            if self.request.user.is_anonymous:
                _creatorName = self.cleaned_data['creator']
                _gameCreator = User(username=_creatorName, email='', password='abc')
                try:
                    _gameCreator.save()
                except IntegrityError:
                    _msg = 'Username unavailable : %s. Please choose another name.' % _creatorName
                    print('CreateGameForm.execute: %s' % _msg)
                    return False, _msg
                except Exception as e:
                    _msg = 'Error : %s %s' % (type(e), e)
                    print('CreateGameForm.execute: %s' % _msg)
                    print('Should implement a non unique User exception here, to manage error message properly')
                    return False, _msg
            else:
                _creatorId = self.request.user.id
                try:
                    _gameCreator = User.objects.get(id=_creatorId)
                except Exception as e:
                    _msg = 'Error while retrieving creator user : %s %s' % (type(e), e)
                    print('CreateGameForm.execute: %s' % _msg)
                    return False, _msg

            # create game
            _gameLogic = game.GameLogic()
            self.game = _gameLogic.createGame(game_name=_gameName, game_genre=_gameGenre, game_creator=_gameCreator)

        except Exception as e:
            print('CreateGameForm.execute: error : %s %s' % (type(e), e))
            return False, e

        print('CreateGameForm.execute: game %s created : %s' % (self.game.name, self.game.id))
        return True, self.game.id

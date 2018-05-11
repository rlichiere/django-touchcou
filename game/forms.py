
from django import forms

from . import models


class CreateGameForm(forms.ModelForm):
    name = forms.CharField(label='Game name')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(CreateGameForm, self).__init__(*args, **kwargs)
        self.game = None

    def execute(self):
        try:
            _gameName = self.cleaned_data['name']
            _gameCreator = self.request.user

            self.game = models.Game(name=_gameName, creator=_gameCreator)
            self.game.save()

        except Exception as e:
            print('CreateGameForm.execute: error : %s %s' % (type(e), e))
            return False, e

        print('CreateGameForm.execute: game %s created : %s' % (self.game.name, self.game.id))
        return True, self.game.id

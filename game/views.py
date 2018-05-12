
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import FormView, TemplateView, DetailView

from . import forms
from . import models


class HomeView(TemplateView):
    template_name = 'game/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context


class GamesListView(TemplateView):
    template_name = 'game/game_list.html'

    def get_context_data(self, **kwargs):
        _l = '%s.get_context_data:' % self.__class__
        context = super(GamesListView, self).get_context_data(**kwargs)

        context['user_games'] = None
        context['opened_games'] = None

        _userGames = list()
        _openedGames = list()
        _user = None
        try:
            # process registered user case
            _user = User.objects.get(id=self.request.user.id)

            # build user games list
            for _userParticipation in models.UserParticipation.objects.filter(user=_user):
                if _userParticipation.game.registrationsOpened():
                    _userGames.append(_userParticipation.game)

            # initialize user's games list
            _games = models.Game.objects.exclude(participations__user=_user)
            print('GamesListView.get_context_data: _games: %s' % _games)

        except User.DoesNotExist as e:
            # process anonymous user case

            # initialize user's games list
            _games = models.Game.objects.all()
        except Exception as e:
            print('%s unexpected error while retrieving user : %s: %s %s' % (_l, self.request.user, type(e), e))
            raise Exception(e)

        # build opened games list
        for _game in _games:
            if not _game.registrationsOpened():
                continue
            _openedGames.append(_game)

        # for _game in _games:
        #     if not _game.registrationsOpened():
        #         continue
        #
        #     if _user is not None:
        #         if _user in _game.players.all():
        #             _userGames.append(_game)
        #         else:
        #             _openedGames.append(_game)
        #     else:
        #         _openedGames.append(_game)

        if len(_userGames) > 0:
            context['user_games'] = _userGames
        if len(_openedGames) > 0:
            context['opened_games'] = _openedGames

        return context


class GameCreateView(FormView):
    template_name = 'game/game_create.html'
    form_class = forms.CreateGameForm
    model = models.Game

    def get_form_kwargs(self):
        kwargs = super(GameCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        (status, msg) = form.execute()
        if not status:
            _msg = 'Error : %s' % msg
            print('GameCreateView.form_valid: %s' % _msg)
            messages.add_message(self.request, messages.ERROR, message=_msg, fail_silently=True)
            return HttpResponseRedirect(reverse('game-home'))
        else:
            _msg = 'Game %s created successfully' % form.game.name
            print('GameCreateView.form_valid: %s' % _msg)
            messages.add_message(self.request, messages.SUCCESS, message=_msg, fail_silently=True)
            # return HttpResponseRedirect(reverse('game-board', kwargs={'game_id': form.game.id}))
            return HttpResponseRedirect(reverse('game-player-prepare', kwargs={'game_id': form.game.id}))

    def form_invalid(self, form):
        _msg = 'Error : %s' % form.errors.as_text()
        print('GameCreateView.form_invalid: %s' % _msg)
        messages.add_message(self.request, messages.ERROR, message=_msg, fail_silently=True)
        return HttpResponseRedirect(reverse('game-home'))


class GamePlayerPrepareView(DetailView):
    model = models.Game
    context_object_name = 'game'
    template_name = 'game/game_player_prepare.html'

    def get_object(self, *args, **kwargs):
        user = get_object_or_404(models.Game, id=self.kwargs['game_id'])
        return user

    """ validates and stores player preparation data """
    def post(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('game-board', kwargs={'game_id': self.kwargs.get('game_id')}))


class GameBoardView(TemplateView):
    template_name = 'game/game_board.html'

    def get_context_data(self, **kwargs):
        context = super(GameBoardView, self).get_context_data(**kwargs)
        context['game_id'] = kwargs.get('game_id')
        return context

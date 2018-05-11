
from django.contrib import messages
from django.http import Http404
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

from django.views.generic import FormView, TemplateView, UpdateView
from django.http import HttpResponseRedirect

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
        context = super(GamesListView, self).get_context_data(**kwargs)

        _games = models.Game.objects.all()
        context['user_games'] = _games.filter(creator=self.request.user)

        _openedGames = list()
        for _game in _games.exclude(creator=self.request.user):
            if self.request.user not in _game.players.all():
                continue
            _openedGames = _game
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
            return HttpResponseRedirect(reverse('game-board', kwargs={'game_id': form.game.id}))

    def form_invalid(self, form):
        _msg = 'Error : %s' % form.errors.as_text()
        print('GameCreateView.form_invalid: %s' % _msg)
        messages.add_message(self.request, messages.ERROR, message=_msg, fail_silently=True)
        return HttpResponseRedirect(reverse('game-home'))


class GameBoardView(TemplateView):
    template_name = 'game/game_board.html'

    def get_context_data(self, **kwargs):
        context = super(GameBoardView, self).get_context_data(**kwargs)
        context['game_id'] = kwargs.get('game_id')
        return context


# class GameJoinView(FormView):
#     template_name = 'game/game_player_join_modal.html'
#     form_class = forms.GameJoinForm
#     model = models.Game
#     # fields = ['player']
#
#     def get_context_data(self, **kwargs):
#         context = super(GameJoinView, self).get_context_data(**kwargs)
#         # context.update({'prod_req': ProductionRequest.objects.get(id=self.kwargs['pk'])})
#         return context
#
#     def form_valid(self, form):
#         game = models.Game.objects.get(id=self.kwargs['game_id'])
#
#         print('GameJoinView.form_valid: %s' % form.cleaned_data['players'])
#         if prod_req.back_to_consult == True:
#             prod_req.tenant_name = form.cleaned_data['tenant_name']
#             prod_req.save()
#         else:
#             form.save(commit=True)
#         return HttpResponseRedirect(reverse('production-request'))
#
#     def form_invalid(self, form):
#         messages.add_message(self.request, messages.ERROR, "One or more invalid form field", fail_silently=True)
#         return HttpResponseRedirect(reverse('production-request'))

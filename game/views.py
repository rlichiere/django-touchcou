
import json
from django.urls import reverse

from django.views.generic import View, FormView, TemplateView
from django.http import HttpResponse, HttpResponseRedirect

from . import forms
from . import models


class HomeView(TemplateView):
    template_name = 'game/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        # show home page
        return context


class CreateGameView(FormView):
    template_name = 'game/game_create.html'
    form_class = forms.CreateGameForm
    model = models.Game

    def get_form_kwargs(self):
        kwargs = super(CreateGameView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        (status, msg) = form.execute()
        if not status:
            print('CreateGameView.form_valid: form.execute error : %s' % msg)
            # messages.add_message(self.request, messages.ERROR, msg, fail_silently=True)
        else:
            print('CreateGameView.form_valid: form executed : %s' % msg)
            # messages.add_message(self.request, messages.INFO, msg, fail_silently=True)

        if not form.game:
            return HttpResponseRedirect(reverse('game-home'))
        else:
            return HttpResponseRedirect(reverse('game-board', kwargs={'game_id': form.game.id}))

    def form_invalid(self, form):
        print('CreateGameView.form_invalid: error : %s' % form.errors.as_text())
        # messages.add_message(self.request, messages.ERROR,
        #                      'One or more invalid form field : %s' % form.errors.as_text(), fail_silently=True)
        return HttpResponseRedirect(reverse('tenant-list'))


class BoardView(TemplateView):
    template_name = 'game/game_board.html'

    def get_context_data(self, **kwargs):
        context = super(BoardView, self).get_context_data(**kwargs)
        context['game_id'] = kwargs.get('game_id')
        return context

    # def get(self, request, *args, **kwargs):
    #     # returns sends CreateGame form
    #     pass
    #
    # def post(self, request, *args, **kwargs):
    #     # create a Game object
    #
    #     _gameName = request.POST.get('game_name', None)
    #     if not _gameName:
    #         return HttpResponse(json.dumps({'error': 'game_name required'}), content_type='application/json', status=500)
    #
    #     return HttpResponse(json.dumps({'game_id': 1}), content_type='application/json')

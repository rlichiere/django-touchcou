
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'touchcou/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        # show home page
        return context

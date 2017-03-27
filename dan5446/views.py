from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import Context, RequestContext
from actstream.models import actor_stream
from django.contrib.auth.decorators import login_required
from brewlog.forms import IngredientForm

class Index(TemplateView):
    content_type = None
    template_name = 'dan5446/index.html'

    def get_context_data(self, **kwargs):
        context = {}
        context['user'] = self.request.user
        context['notifications'] = actor_stream(self.request.user)
        context['form'] = IngredientForm()
        return RequestContext(self.request, context)



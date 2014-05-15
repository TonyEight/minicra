import datetime
import calendar
import json
from django.views.generic import (
    TemplateView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView
)
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from braces.views import LoginRequiredMixin
from django_filters.views import FilterView
from business_context.models import (
    Organisation,
    Client,
    Contract
)
from activity.models import (
    DeclaredDay,
    Month,
    Report
)


class AjaxableResponseMixin(object):

    def render_to_json_response(self, context, **response_kwargs):
        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(data, **response_kwargs)

    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return self.render_to_json_response(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {}
            if hasattr(self, 'object'):
                data.update({
                    'pk': self.object.pk,
                })
            else:
                data.update({
                    'object_list': object_list,
                })
            return self.render_to_json_response(data)
        else:
            return response

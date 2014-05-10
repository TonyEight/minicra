import datetime
import calendar
from django.views.generic import TemplateView
from django.db.models import Q
from django.db.models import Sum
from django.core.urlresolvers import reverse
from braces.views import LoginRequiredMixin
from django_filters.views import FilterView
from activity.models import (
    Activity,
    OffDay,
    Month,
    Report,
)
from context.models import (
    Organisation,
    Client,
    Contract,
    Project,
)
from activity.views import (
    ActivityCreateView,
)
from frontend.forms import (
    ActivityForm,
)
from frontend.filters import (
    ActivityFilter,
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
            data = {
                'pk': self.object.pk,
            }
            return self.render_to_json_response(data)
        else:
            return response


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'frontend/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        today = datetime.date.today()
        contracts = Contract.objects.filter(
            Q(end__gte=today) | Q(end__isnull=True),
            actor=self.request.user
        )
        current_month, created = Month.objects.get_or_create(
            month=today.month,
            year=today.year
        )
        reports = Report.objects.filter(
            month=current_month
        )
        days_with_activity = reports.aggregate(
            sum=Sum('days_with_activity')
        )['sum']
        offdays = reports.aggregate(
            sum=Sum('off_days')
        )['sum']
        calendar_html = calendar.HTMLCalendar().formatmonth(
            current_month.year, 
            current_month.month, 
            True
        )
        calendar_html = calendar_html.replace(
            'border="0" cellpadding="0" cellspacing="0" class="month"', 
            'class="table table-bordered table-condensed" id="dashboard-calendar"'
        )
        calendar_html = calendar_html.replace(
            '">' + str(today.day) + '<', 
            ' today">' + str(today.day) + '<'
        )
        context.update({
            'contracts': contracts,
            'reports': reports,
            'days_with_activity': days_with_activity,
            'offdays': offdays,
            'calendar': calendar_html,
            'current_month': current_month
        })
        return context


class TraceMyActivityView(LoginRequiredMixin, FilterView):
    template_name = 'frontend/activity/trace_activity.html'
    filterset_class = ActivityFilter

    def get_queryset(self):
        return Activity.objects.filter(
            contract__actor=self.request.user
        )

    def get_context_data(self, **kwargs):
        context = super(TraceMyActivityView, self).get_context_data(**kwargs)
        try:
            current_month = Month.objects.get(
                month=int(self.filterset.form.cleaned_data['month']),
                year=int(self.filterset.form.cleaned_data['year'])
            )
        except:
            try:
                current_month = {
                    'month': int(self.filterset.form.cleaned_data['month']),
                    'year': int(self.filterset.form.cleaned_data['year'])
                }
            except:
                current_month = None
        context.update({
            'activity_form': ActivityForm(),
            'current_month': current_month
        })
        return context


class CreateActivityView(LoginRequiredMixin, AjaxableResponseMixin, ActivityCreateView):
    template_name = 'frontend/activity/create_activity.html'

    def get_success_url(self):
        return reverse('trace-activity')
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
from django.db.models import Q
from django.db.models import Sum
from django.core.urlresolvers import reverse
from django.http import HttpResponse
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
from frontend.forms import (
    ActivityForm,
    OffDayForm,
)
from frontend.filters import (
    ActivityFilter,
    OffDayFilter,
    ReportFilter
)


class AjaxableResponseMixin(object):
    def render_to_json_response(self, context, **response_kwargs):
        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(data, **response_kwargs)

    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        print self.request.is_ajax()
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
                'url': self.get_success_url(),
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
            month=current_month,
            contract__in=contracts
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
            'current_month': current_month,
            'user_has_activity': len(self.get_queryset())
        })
        return context


class CreateActivityView(LoginRequiredMixin, AjaxableResponseMixin, CreateView):
    model = Activity
    template_name = 'frontend/activity/activity_form.html'
    form_class = ActivityForm

    def get_success_url(self):
        return reverse('trace-activity')


class UpdateActivityView(LoginRequiredMixin, AjaxableResponseMixin, UpdateView):
    model = Activity
    template_name = 'frontend/activity/activity_form.html'

    def get_initial(self):
        initial = super(UpdateActivityView, self).get_initial()
        initial['date'] = self.object.date.strftime('%m/%d/%Y')
        return initial

    def get_success_url(self):
        return reverse('trace-activity')


class DeleteActivityView(LoginRequiredMixin, AjaxableResponseMixin, DeleteView):
    model = Activity

    def get_success_url(self):
        return reverse('trace-activity')


class TraceMyOffDayView(LoginRequiredMixin, FilterView):
    template_name = 'frontend/activity/trace_offday.html'
    filterset_class = OffDayFilter

    def get_queryset(self):
        return OffDay.objects.filter(
            contract__actor=self.request.user
        )

    def get_context_data(self, **kwargs):
        context = super(TraceMyOffDayView, self).get_context_data(**kwargs)
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
            'current_month': current_month,
            'user_has_offday': len(self.get_queryset())
        })
        return context


class CreateOffDayView(LoginRequiredMixin, AjaxableResponseMixin, CreateView):
    model = OffDay
    template_name = 'frontend/activity/offday_form.html'
    form_class = OffDayForm

    def get_success_url(self):
        return reverse('trace-offday')

class UpdateOffDayView(LoginRequiredMixin, AjaxableResponseMixin, UpdateView):
    model = OffDay
    template_name = 'frontend/activity/offday_form.html'

    def get_initial(self):
        initial = super(UpdateOffDayView, self).get_initial()
        initial['date'] = self.object.date.strftime('%m/%d/%Y')
        return initial

    def get_success_url(self):
        return reverse('trace-offday')

class DeleteOffDayView(LoginRequiredMixin, AjaxableResponseMixin, DeleteView):
    model = OffDay

    def get_success_url(self):
        return reverse('trace-offday')


class ReportListView(LoginRequiredMixin, FilterView):
    template_name = 'frontend/activity/report_list.html'
    filterset_class = ReportFilter

    def get_queryset(self):
        return Report.objects.filter(
            contract__actor=self.request.user
        ).order_by('-month')

    def get_context_data(self, **kwargs):
        context = super(ReportListView, self).get_context_data(**kwargs)
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
            'current_month': current_month,
            'reports': Report.get_reports_for(self.request.user)
        })
        return context


class ReportDetailView(LoginRequiredMixin, DetailView):
    model = Report
    template_name = 'frontend/activity/report_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ReportDetailView, self).get_context_data(**kwargs)
        rq = self.request.GET
        query = '?year=%s&month=%s&contract=%s' % (rq.get('year',''), rq.get('month',''), rq.get('contract',''))
        context.update({
            'return_link': reverse('list-report') + query
        })
        return context
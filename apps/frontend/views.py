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
    DeclaredDay,
    Month,
    Report,
)
from context.models import (
    Contract
)
from frontend.forms import (
    DeclaredDayForm
)
from frontend.filters import (
    DeclaredDayFilter,
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
            month=current_month,
            contract__in=contracts
        )
        days_with_activity = reports.aggregate(
            sum=Sum('days_with_activity')
        )['sum']
        off_days = reports.aggregate(
            sum=Sum('off_days')
        )['sum']
        context.update({
            'contracts': contracts,
            'reports': reports,
            'days_with_activity': days_with_activity,
            'off_days': off_days,
            'current_month': current_month
        })
        return context


class TraceMyActivityView(LoginRequiredMixin, FilterView):
    template_name = 'frontend/activity/trace_activity.html'
    filterset_class = DeclaredDayFilter

    def get_queryset(self):
        return DeclaredDay.objects.filter(
            contract__actor=self.request.user,
            type=1
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


class CreateActivityView(LoginRequiredMixin, 
                         AjaxableResponseMixin, CreateView):
    model = DeclaredDay
    template_name = 'frontend/activity/activity_form.html'
    form_class = DeclaredDayForm

    def get_success_url(self):
        return reverse('trace-activity')

    def form_valid(self, form):
        form.instance.type = 1
        return super(CreateActivityView, self).form_valid(form)


class UpdateActivityView(LoginRequiredMixin, 
                         AjaxableResponseMixin, UpdateView):
    model = DeclaredDay
    template_name = 'frontend/activity/activity_form.html'
    form_class = DeclaredDayForm

    def get_initial(self):
        initial = super(UpdateActivityView, self).get_initial()
        initial['date'] = self.object.date.strftime('%m/%d/%Y')
        return initial

    def get_success_url(self):
        return reverse('trace-activity')

    def form_valid(self, form):
        form.instance.type = 1
        return super(UpdateActivityView, self).form_valid(form)


class DeleteActivityView(LoginRequiredMixin, 
                         AjaxableResponseMixin, DeleteView):
    model = DeclaredDay

    def get_success_url(self):
        return reverse('trace-activity')


class TraceMyOffDayView(LoginRequiredMixin, FilterView):
    template_name = 'frontend/activity/trace_offday.html'
    filterset_class = DeclaredDayFilter

    def get_queryset(self):
        return DeclaredDay.objects.filter(
            contract__actor=self.request.user,
            type=2
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
    model = DeclaredDay
    template_name = 'frontend/activity/offday_form.html'
    form_class = DeclaredDayForm

    def get_success_url(self):
        return reverse('trace-offday')

    def form_valid(self, form):
        form.instance.type = 2
        return super(CreateOffDayView, self).form_valid(form)

class UpdateOffDayView(LoginRequiredMixin, AjaxableResponseMixin, UpdateView):
    model = DeclaredDay
    template_name = 'frontend/activity/offday_form.html'
    form_class = DeclaredDayForm

    def get_initial(self):
        initial = super(UpdateOffDayView, self).get_initial()
        initial['date'] = self.object.date.strftime('%m/%d/%Y')
        return initial

    def get_success_url(self):
        return reverse('trace-offday')

    def form_valid(self, form):
        form.instance.type = 2
        return super(UpdateOffDayView, self).form_valid(form)

class DeleteOffDayView(LoginRequiredMixin, AjaxableResponseMixin, DeleteView):
    model = DeclaredDay

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
        query = '?year=%s&month=%s&contract=%s' % (
            rq.get('year',''), 
            rq.get('month',''), 
            rq.get('contract','')
        )
        month_dates = []
        for date in self.object.month.dates_list():
            act = None
            off = None
            try:
                act = DeclaredDay.objects.get(
                    date__day=date[0],
                    type=1,
                    date__month=self.object.month.month,
                    date__year=self.object.month.year,
                    contract=self.object.contract
                )
            except:
                pass
            try:
                off = DeclaredDay.objects.get(
                    date__day=date[0],
                    type=2,
                    date__month=self.object.month.month,
                    date__year=self.object.month.year,
                    contract=self.object.contract
                )
            except:
                pass
            month_dates.append({
                'date': date,
                'activity': act,
                'offday': off
            })
        context.update({
            'return_link': reverse('list-report') + query,
            'dates': month_dates
        })
        return context

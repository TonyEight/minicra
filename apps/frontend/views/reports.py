from frontend.views.base import *
from frontend.filters import (
    ReportFilter
)


class ListReportView(LoginRequiredMixin, FilterView):
    template_name = 'frontend/activity/report_list.html'
    filterset_class = ReportFilter

    def get_queryset(self):
        return Report.objects.filter(
            contract__actor=self.request.user
        ).order_by('-month')

    def get_context_data(self, **kwargs):
        context = super(ListReportView, self).get_context_data(**kwargs)
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


class DetailReportView(LoginRequiredMixin, DetailView):
    model = Report
    template_name = 'frontend/activity/report_detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailReportView, self).get_context_data(**kwargs)
        rq = self.request.GET
        query = '?year=%s&month=%s&contract=%s' % (
            rq.get('year', ''),
            rq.get('month', ''),
            rq.get('contract', '')
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

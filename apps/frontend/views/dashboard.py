from django.db.models import Q
from django.db.models import Sum
from frontend.views.base import *


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

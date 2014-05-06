import datetime
from django.views.generic import TemplateView
from django.db.models import Q
from braces.views import LoginRequiredMixin
from activity.models import (
    Activity,
    OffDay,
    Report,
)
from context.models import (
    Organisation,
    Client,
    Contract,
    Project
)

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'frontend/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        contracts = Contract.objects.filter(
            Q(end__gte=datetime.date.today()) | Q(end__isnull=False),
            actor=self.request.user
        )
        context.update({
            'contracts': contracts,
        })
        return context
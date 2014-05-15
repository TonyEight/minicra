from frontend.views.base import *
from frontend.forms import (
    DeclaredDayForm
)
from frontend.filters import (
    DeclaredDayFilter
)


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

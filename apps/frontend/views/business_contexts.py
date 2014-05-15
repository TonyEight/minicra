from frontend.views.base import *
from frontend.forms import (
    OrganisationForm,
    ClientForm,
    ContractForm
)
from frontend.filters import (
    ContractFilter,
    ClientFilter,
    OrganisationFilter
)


class ManageMyBusinessContextView(LoginRequiredMixin, TemplateView):
    template_name = 'frontend/business_context/manage_context.html'

    def get_context_data(self, **kwargs):
        context = super(ManageMyBusinessContextView, self).get_context_data(
            **kwargs
        )
        user_organisations = Organisation.objects.filter(
            actor=self.request.user
        )
        organisation_filter = OrganisationFilter(
            queryset=user_organisations
        )
        user_clients = Client.objects.filter(
            actor=self.request.user
        )
        client_filter = ClientFilter(
            queryset=user_clients
        )
        user_contracts = Contract.objects.filter(
            actor=self.request.user
        )
        contract_filter = ContractFilter(
            queryset=user_clients
        )
        client_filter.form.fields['organisation']\
                          .queryset = user_organisations
        contract_filter.form.fields['client']\
                            .queryset = user_clients
        context.update({
            'user_has_organisations': len(user_organisations),
            'organisation_filter': organisation_filter,
            'user_has_clients': len(user_clients),
            'client_filter': client_filter,
            'user_has_contracts': len(user_contracts),
            'contract_filter': contract_filter
        })
        return context


class ListOrganisationView(LoginRequiredMixin, FilterView):
    template_name = 'frontend/business_context/organisation_list.html'
    filterset_class = OrganisationFilter

    def get_queryset(self):
        return Organisation.objects.filter(
            actor=self.request.user
        ).order_by('name')

    def get_context_data(self, **kwargs):
        context = super(ListOrganisationView, self).get_context_data(**kwargs)
        context.update({
            'user_has_organisations': len(self.get_queryset())
        })
        return context


class CreateOrganisationView(LoginRequiredMixin,
                             AjaxableResponseMixin, CreateView):
    model = Organisation
    template_name = 'frontend/business_context/organisation_form.html'
    form_class = OrganisationForm

    def get_success_url(self):
        return reverse('manage-context')

    def form_valid(self, form):
        form.instance.actor = self.request.user
        return super(CreateOrganisationView, self).form_valid(form)


class UpdateOrganisationView(LoginRequiredMixin,
                             AjaxableResponseMixin, UpdateView):
    model = Organisation
    template_name = 'frontend/business_context/organisation_form.html'
    form_class = OrganisationForm

    def get_success_url(self):
        return reverse('manage-context')


class DeleteOrganisationView(LoginRequiredMixin,
                             AjaxableResponseMixin, DeleteView):
    model = Organisation

    def get_success_url(self):
        return reverse('manage-context')


class ListClientView(LoginRequiredMixin, FilterView):
    template_name = 'frontend/business_context/client_list.html'
    filterset_class = ClientFilter

    def get_queryset(self):
        return Client.objects.filter(
            actor=self.request.user
        ).order_by('name')

    def get_context_data(self, **kwargs):
        context = super(ListClientView, self).get_context_data(**kwargs)
        context.update({
            'user_has_clients': len(self.get_queryset())
        })
        return context


class CreateClientView(LoginRequiredMixin,
                       AjaxableResponseMixin, CreateView):
    model = Client
    template_name = 'frontend/business_context/client_form.html'
    form_class = ClientForm

    def get_success_url(self):
        return reverse('manage-context')

    def form_valid(self, form):
        form.instance.actor = self.request.user
        return super(CreateClientView, self).form_valid(form)

    def get_form(self, *args, **kwargs):
        form = super(CreateClientView, self).get_form(*args, **kwargs)
        form.fields['organisation'].queryset = Organisation.objects.filter(
            actor=self.request.user
        )
        return form


class UpdateClientView(LoginRequiredMixin,
                       AjaxableResponseMixin, UpdateView):
    model = Client
    template_name = 'frontend/business_context/client_form.html'
    form_class = ClientForm

    def get_success_url(self):
        return reverse('manage-context')

    def get_form(self, *args, **kwargs):
        form = super(UpdateClientView, self).get_form(*args, **kwargs)
        form.fields['organisation'].queryset = Organisation.objects.filter(
            actor=self.request.user
        )
        return form


class DeleteClientView(LoginRequiredMixin,
                       AjaxableResponseMixin, DeleteView):
    model = Client

    def get_success_url(self):
        return reverse('manage-context')


class ListContractView(LoginRequiredMixin, FilterView):
    template_name = 'frontend/business_context/contract_list.html'
    filterset_class = ContractFilter

    def get_queryset(self):
        return Contract.objects.filter(
            actor=self.request.user
        ).order_by('name')

    def get_context_data(self, **kwargs):
        context = super(ListContractView, self).get_context_data(**kwargs)
        context.update({
            'user_has_contracts': len(self.get_queryset())
        })
        return context


class CreateContractView(LoginRequiredMixin,
                         AjaxableResponseMixin, CreateView):
    model = Contract
    template_name = 'frontend/business_context/contract_form.html'
    form_class = ContractForm

    def get_success_url(self):
        return reverse('manage-context')

    def form_valid(self, form):
        form.instance.actor = self.request.user
        return super(CreateContractView, self).form_valid(form)

    def get_form(self, *args, **kwargs):
        form = super(CreateContractView, self).get_form(*args, **kwargs)
        form.fields['client'].queryset = Client.objects.filter(
            actor=self.request.user
        )
        return form


class UpdateContractView(LoginRequiredMixin,
                         AjaxableResponseMixin, UpdateView):
    model = Contract
    template_name = 'frontend/business_context/contract_form.html'
    form_class = ContractForm

    def get_success_url(self):
        return reverse('manage-context')

    def get_form(self, *args, **kwargs):
        form = super(UpdateContractView, self).get_form(*args, **kwargs)
        form.fields['client'].queryset = Client.objects.filter(
            actor=self.request.user
        )
        return form


class DeleteContractView(LoginRequiredMixin,
                         AjaxableResponseMixin, DeleteView):
    model = Contract

    def get_success_url(self):
        return reverse('manage-context')

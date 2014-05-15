from django import forms
from business_context.models import (
    Organisation,
    Client,
    Contract
)
from activity.models import (
    DeclaredDay
)


class OrganisationForm(forms.ModelForm):

    class Meta:
        model = Organisation
        fields = '__all__'
        exclude = ('actor',)


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = '__all__'
        exclude = ('actor',)


class ContractForm(forms.ModelForm):

    class Meta:
        model = Contract
        fields = '__all__'
        exclude = ('actor',)


class DeclaredDayForm(forms.ModelForm):

    class Meta:
        model = DeclaredDay
        fields = '__all__'
        exclude = ('type',)

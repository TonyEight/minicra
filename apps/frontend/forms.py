from __future__ import unicode_literals
from django import forms
from business_context.models import (
    Organisation,
    Client,
    Contract
)
from activity.models import (
    DeclaredDay
)


class BootstrapForm(forms.ModelForm):
    # Methods
    def __init__(self, *args, **kwargs):
        super(BootstrapForm, self).__init__(*args, **kwargs)
        # we iterate through all fields of the form
        for name, field in self.fields.items():
            # we set the Bootstrap CSS class
            if field.widget.attrs.has_key('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs.update({'class':'form-control'})


class OrganisationForm(BootstrapForm):

    class Meta:
        model = Organisation
        fields = '__all__'
        exclude = ('actor',)


class ClientForm(BootstrapForm):

    class Meta:
        model = Client
        fields = '__all__'
        exclude = ('actor',)


class ContractForm(BootstrapForm):

    class Meta:
        model = Contract
        fields = '__all__'
        exclude = ('actor',)


class DeclaredDayForm(BootstrapForm):

    class Meta:
        model = DeclaredDay
        fields = '__all__'
        exclude = ('type',)

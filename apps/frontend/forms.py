from __future__ import unicode_literals
import datetime
from django import forms
from django.utils.translation import ugettext_lazy as _
from business_context.models import (
    Organisation,
    Client,
    Contract
)
from activity.models import (
    DeclaredDay
)


class DateRangeWidget(forms.MultiWidget):
    def __init__(self, attrs=None, date_format=None,):
        widgets = (
            forms.DateInput(attrs=attrs, format=date_format),
            forms.DateInput(attrs=attrs, format=date_format)
        )
        super(DateRangeWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            dates = value.split(' # ')
            if len(dates) == 2:
                return [
                    datetime.datetime.strptime(dates[0], '%d/%m/%Y').date(), 
                    datetime.datetime.strptime(dates[1], '%d/%m/%Y').date()
                ]
        return [None, None]


class DateRangeField(forms.MultiValueField):
    widget = DateRangeWidget

    def __init__(self, *args, **kwargs):
        # Define one message for all fields.
        error_messages = {
            'incomplete': _('Enter a start date and an end date.'),
        }
        # Or define a different message for each field.
        fields = (
            forms.DateField(),
            forms.DateField(),
        )
        super(DateRangeField, self).__init__(
            error_messages=error_messages, fields=fields,
            require_all_fields=True, *args, **kwargs)

    def compress(self, data_list):
        return ' # '.join([unicode(date) for date in data_list])


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

from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from parameters.models import PublicHoliday


class PublicHolidayForm(forms.ModelForm):
    date = forms.DateField(required=True)

    class Meta:
        model = PublicHoliday
        fields = ('name', 'is_fixed')

    def save(self, force_insert=False, force_update=False, commit=True):
        holiday = super(PublicHolidayForm, self).save(commit=False)
        date = self.cleaned_data['date']
        holiday.day = date.day
        holiday.month = date.month
        if not holiday.is_fixed:
            holiday.year = date.year
        if commit:
            holiday.save()
        return holiday


class PublicHolidayAdminForm(PublicHolidayForm):
    def __init__(self, *args, **kwargs):
        super(PublicHolidayAdminForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget = AdminDateWidget()

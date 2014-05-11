from django import forms
from activity.models import (
    Activity,
    OffDay
)


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'


class OffDayForm(forms.ModelForm):
    class Meta:
        model = OffDay
        fields = '__all__'
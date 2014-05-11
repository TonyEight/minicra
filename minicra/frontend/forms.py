from django import forms
from activity.models import (
    DeclaredDay
)


class DeclaredDayForm(forms.ModelForm):
    class Meta:
        model = DeclaredDay
        fields = '__all__'
        exclude = ('type',)
from django import forms
from activity.models import (
    Activity,
    Report
)


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'

    class Media:
        css = {
            'all': (
                'http://eternicode.github.io/bootstrap-datepicker/'
                'bootstrap-datepicker/css/datepicker3.css',
            )
        }
        js = (
            'http://eternicode.github.io/bootstrap-datepicker/'
            'bootstrap-datepicker/js/bootstrap-datepicker.js',
        )


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = '__all__'

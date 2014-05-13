import datetime
import django_filters
from activity.models import (
    DeclaredDay,
    Month,
    Report,
)


def get_years():
    current_year = datetime.date.today().year
    years = []
    years.append((None, 'Any year'))
    for y in range(current_year-5, current_year+6):
        years.append((y, str(y)))
    return years

def get_months():
    months = []
    months.append((None, 'Any month'))
    months += Month.MONTHS
    return months

def get_periods():
    periods = []
    periods.append((None, 'Any period'))
    periods += DeclaredDay.PERIODS
    return periods


class DeclaredDayFilter(django_filters.FilterSet):
    month = django_filters.ChoiceFilter(
        choices=get_months(), 
        name='date',
        lookup_type='month'
    )
    year = django_filters.ChoiceFilter(
        choices=get_years(), 
        name='date',
        lookup_type='year'
    )
    period = django_filters.ChoiceFilter(
        choices=get_periods(),
    )

    class Meta:
        model = DeclaredDay
        fields = ['period', 'contract']

    def __init__(self, *args, **kwargs):
        super(DeclaredDayFilter, self).__init__(*args, **kwargs)
        self.filters['contract'].extra.update(
            {'empty_label': 'Any contract'}
        )
        for name, field in self.form.fields.items():
            if field.widget.attrs.has_key('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs.update({'class':'form-control'})


class ReportFilter(django_filters.FilterSet):
    month = django_filters.ChoiceFilter(
        choices=get_months(), 
        name='month',
        lookup_type='month'
    )
    year = django_filters.ChoiceFilter(
        choices=get_years(), 
        name='month',
        lookup_type='year'
    )

    class Meta:
        model = Report
        fields = ['contract']

    def __init__(self, *args, **kwargs):
        super(ReportFilter, self).__init__(*args, **kwargs)
        self.filters['contract'].extra.update(
            {'empty_label': 'Any contract'}
        )
        for name, field in self.form.fields.items():
            if field.widget.attrs.has_key('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs.update({'class':'form-control'})
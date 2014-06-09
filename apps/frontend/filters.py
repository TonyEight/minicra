from __future__ import unicode_literals
import datetime
import django_filters
from business_context.models import (
    Organisation,
    Client,
    Contract
)
from activity.models import (
    DeclaredDay,
    Month,
    Report,
)


def get_years():
    current_year = datetime.date.today().year
    years = []
    years.append((None, 'Any year'))
    for y in range(current_year - 5, current_year + 6):
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


class FrontEndFilter(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        super(FrontEndFilter, self).__init__(*args, **kwargs)
        for name, filter_obj in self.filters.items():
            if type(filter_obj) == django_filters.ModelChoiceFilter:
                self.filters[name].extra.update(
                    {'empty_label': 'Any %s' % name.lower()}
                )
        for name, field in self.form.fields.items():
            if 'class' in field.widget.attrs:
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs.update({'class': 'form-control'})


class ContractFilter(FrontEndFilter):
    mission = django_filters.CharFilter(
        lookup_type=(
            'contains',
            'exact',
            'startswith',
            'endswith',
        )
    )
    description = django_filters.CharFilter(
        lookup_type=(
            'contains',
            'startswith',
            'endswith',
        )
    )
    project = django_filters.CharFilter(
        lookup_type=(
            'contains',
            'exact',
            'startswith',
            'endswith',
        )
    )
    start_month = django_filters.ChoiceFilter(
        choices=get_months(),
        label='start month',
        name='start',
        lookup_type='month'
    )
    start_year = django_filters.ChoiceFilter(
        choices=get_years(),
        label='start year',
        name='end',
        lookup_type='year'
    )
    end_month = django_filters.ChoiceFilter(
        choices=get_months(),
        label='end month',
        name='end',
        lookup_type='month'
    )
    end_year = django_filters.ChoiceFilter(
        choices=get_years(),
        label='end year',
        name='end',
        lookup_type='year'
    )
    sold_days = django_filters.NumberFilter(
        lookup_type=(
            'gt',
            'gte',
            'exact',
            'lt',
            'lte',
        )
    )

    class Meta:
        model = Contract
        fields = ['mission', 'description', 'client', 'project', 'sold_days']


class ClientFilter(FrontEndFilter):
    name = django_filters.CharFilter(
        lookup_type=(
            'contains',
            'exact',
            'startswith',
            'endswith',
        )
    )
    service = django_filters.CharFilter(
        lookup_type=(
            'contains',
            'exact',
            'startswith',
            'endswith',
        )
    )

    class Meta:
        model = Client
        fields = ['name', 'service', 'organisation']


class OrganisationFilter(FrontEndFilter):
    name = django_filters.CharFilter(
        lookup_type=(
            'contains',
            'exact',
            'startswith',
            'endswith',
        )
    )

    class Meta:
        model = Organisation
        fields = ['name']


class DeclaredDayFilter(FrontEndFilter):
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


class ReportFilter(FrontEndFilter):
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

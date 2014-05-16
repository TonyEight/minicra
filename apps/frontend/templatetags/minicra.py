import datetime
import calendar
from django import template
from django.core.urlresolvers import reverse
from django.db.models import Q
from parameters.models import PublicHoliday

register = template.Library()


@register.simple_tag
def active(request, pattern):
    path = request.path
    if path == reverse(pattern):
        return 'active'
    return ''


@register.filter(name='beautify')
def beautify_days_number(value):
    return str(value).replace('.0', '')


@register.inclusion_tag('frontend/extra/greetings.html', takes_context=True)
def greetings(context):
    now = datetime.datetime.now()
    username = context['user_display']
    if username != '':
        username = context['user_display_short']
    return {
        'username': username,
        'hour': now.hour
    }


@register.inclusion_tag('frontend/extra/month_calendar.html',
                        takes_context=True)
def month_calendar(context, year, month, calendar_id, with_year=True,
                   today_css_class='today', with_holidays=True,
                   holidays_css_class='holiday', noday_css_class='noday'):
    today = datetime.date.today()
    if not year:
        year = today.year
    if not month:
        month = today.month
    cal = calendar.HTMLCalendar()
    tag_context = {
        'calendar_header': cal.formatmonthname(
            year,
            month,
            withyear=with_year
        ),
        'calendar_week_header': cal.formatweekheader(),
        'weeks': cal.monthdays2calendar(
            year,
            month
        ),
        'calendar_id': calendar_id,
        'today_css_class': today_css_class,
        'holidays_css_class': holidays_css_class,
        'noday_css_class': noday_css_class
    }
    holidays = []
    holidays_list = []
    if with_holidays:
        h = holidays.append
        holidays_list = PublicHoliday.objects.filter(
            Q(month=month, year=year) |
            Q(month=month, is_fixed=True)
        )
        for date in holidays_list:
            h(date.day)
    if today.month == month and today.year == year:
        tag_context.update({
            'today': today.day
        })
    tag_context.update({
        'year': year,
        'holidays': holidays,
        'holidays_list': holidays_list
    })
    return tag_context

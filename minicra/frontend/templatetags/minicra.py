import datetime
import calendar
from django import template
from django.core.urlresolvers import reverse

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
                   today_css_class='today', with_off_days=True,
                   off_css_class='off', with_activity=True,
                   activity_css_class='act', noday_css_class='noday'):
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
        'off_css_class': off_css_class,
        'activity_css_class': activity_css_class,
        'noday_css_class': noday_css_class
    }
    days_with_activity = []
    days_off = []
    if with_activity:
        a = days_with_activity.append
        user = context['user']
        for c in user.contracts.all():
            for d in c.activities.filter(
                date__month=month,
                date__year=year
            ):
                a(d.date.day)
    if with_off_days:
        o = days_off.append
        user = context['user']
        for c in user.contracts.all():
            for d in c.off_days.filter(
                date__month=month,
                date__year=year
            ):
                o(d.date.day)
    if today.month == month and today.year == year:
        tag_context.update({
            'today': today.day
        })
    tag_context.update({
        'days_with_activity': days_with_activity,
        'days_off': days_off,
    })
    return tag_context

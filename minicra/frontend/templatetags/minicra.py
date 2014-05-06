from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.simple_tag
def active(request, pattern):
    path = request.path
    if path == reverse(pattern):
        return 'active'
    return ''
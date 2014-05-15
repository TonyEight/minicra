import datetime
from django.contrib.auth.models import AnonymousUser


def display_user(request):
    user_display = ''
    user_display_short = ''
    if not request.user.is_anonymous():
        if request.user.first_name:
            user_display_short = request.user.first_name
            if request.user.last_name:
                user_display = request.user.get_full_name()
        else:
            user_display = request.user.username
    return {
        'user_display': user_display,
        'user_display_short': user_display_short
    }

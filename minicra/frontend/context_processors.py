def display_user(request):
    try:
        if request.user.first_name and request.user.last_name:
            print request.user
            return {
                'user_display': request.user.get_full_name()
            }
        else:
            return {
                'user_display': request.user.username
            }
    except:
        return ''
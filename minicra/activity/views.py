from django.views.generic import (
    CreateView,
    ListView
)
from activity.models import Activity


class ActivityCreateView(CreateView):
    model = Activity

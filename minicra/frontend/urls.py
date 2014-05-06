from django.conf.urls import include, url
from frontend.views import (
    DashboardView
)

urlpatterns = [
    url(r'^$', DashboardView.as_view(), name='dashboard'),
]
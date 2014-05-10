from django.conf.urls import include, url
from frontend.views import (
    DashboardView,
    TraceMyActivityView,
    CreateActivityView,
)

urlpatterns = [
    url(r'^$', DashboardView.as_view(), name='dashboard'),
    url(r'^activity/$', TraceMyActivityView.as_view(), name='trace-activity'),
    url(r'^activity/add/$', CreateActivityView.as_view(), name='create-activity'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'frontend/auth/login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'^password_change/$', 'django.contrib.auth.views.password_change', {'template_name': 'frontend/auth/password_change_form.html'}, name='password_change'),
    url(r'^password_change/done/$', 'django.contrib.auth.views.password_change_done', {'template_name': 'frontend/auth/password_change_done.html'}, name='password_change_done'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', {'template_name': 'frontend/auth/password_reset_form.html', 'email_template_name': 'frontend/auth/password_reset_email.html'}, name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', {'template_name': 'frontend/auth/password_reset_done.html'}, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 'django.contrib.auth.views.password_reset_confirm', {'template_name': 'frontend/auth/password_reset_confirm.html'}, name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', {'template_name': 'frontend/auth/password_reset_complete.html'}, name='password_reset_complete'),
]
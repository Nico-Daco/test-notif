from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from devices import views

urlpatterns = [
    url(r'^accounts/(?P<account_id>\d+)/profiles/(?P<profile_id>\d+)/$',
        views.AccountView.as_view()),
    url(r'^notifications/$',
        views.NotificationsView.as_view()),
    ]

from django.conf.urls import url

from django.utils import timezone

from . import views

app_name = "timetracker"

monthdateyrREGEX = r'(?P<month>[0-9]{1,2})/(?P<day>[0-9]{1,2})/(?P<year>[0-9]{1,4})'

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^' + monthdateyrREGEX + '/edit/$', views.edit_day, name='edit_day'),
    url(r'^' + monthdateyrREGEX + '/view/$', views.view_day, name="view_day"),
    url(r'^test/$', views.test, name='test'),
]
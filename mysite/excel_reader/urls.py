from django.conf.urls import url

from django.contrib.auth.views import login


from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<excel_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^input/$', views.input_file, name="input"),
    url(r'^login/', view=login, kwargs={'template_name': 'login.html'}, name='login'),
]
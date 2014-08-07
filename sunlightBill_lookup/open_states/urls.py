from django.conf.urls import patterns, url

from open_states import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^get_widget_list/(?P<bill_id>\d+)/(?P<state>\S+?)/$', views.get_widget_list, name='get_widget list'),
)
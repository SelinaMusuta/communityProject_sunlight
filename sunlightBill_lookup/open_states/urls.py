from django.conf.urls import patterns, url

from open_states import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^get_widget_list/(?P<sunlightAPIs>.+?)/(?P<bill_id>.+?)/(?P<state>\S+?)/$', views.get_widget_list, name='get_widget list'),
    url(r'^get_widget_list/(?P<sunlightAPIs>.+?)/(?P<bill_id>.+?)/$', views.get_widget_list, name='get_widget_congress list'),
)

# Note that in the get_widget_list url, we need to give it a place to accept both the bill_id as a number and the state ID as a string
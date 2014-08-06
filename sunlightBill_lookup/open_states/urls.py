from django.conf.urls import patterns, url

from open_states import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<bill_id>.*?)/(?P<state>.*?)/$', views.get_widget_list, name='widget_list_by_state_and_bill')
     #url(r'^widget_list/$', views.get_widget_list, name='widget list')
)

#widget_list/
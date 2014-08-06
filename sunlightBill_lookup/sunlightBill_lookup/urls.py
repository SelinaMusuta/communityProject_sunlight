from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sunlightBill_lookup.views.home', name='home'),
	url(r'^open_states/', include('open_states.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

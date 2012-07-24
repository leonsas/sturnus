from django.conf.urls.defaults import patterns, include, url
from sturnus.views import home, json_builder, json_server
from django.conf import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sturnus.views.home', name='home'),
   (r'^user_id/(?P<user_id>\d{0,30})/$', json_builder),
   (r'^(?P<screenname>\w{0,40})/$', home),
   (r'^$', home),
   (r'^files/(?P<path>.*)$', 'django.views.static.serve',                {'document_root': settings.MEDIA_ROOT }),
   (r'^dynamic/(?P<user_id>\w{0,40}).json/$', json_server),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

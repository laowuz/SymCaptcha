from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()
handler404 = 'django.views.defaults.page_not_found'
handler500 = 'django.views.defaults.server_error'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^polls/',include('polls.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^captcha/',include('captcha.urls')),
    url(r'^captcha/tests/',include('captcha.tests.urls')),
    url(r'^symcaptcha/',include('symcaptcha.urls')),
    url(r'^indexer/',include('indexer.urls')),
)

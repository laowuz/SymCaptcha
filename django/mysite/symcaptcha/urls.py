from django.conf.urls.defaults import *

urlpatterns = patterns('',
        url(r'^$','symcaptcha.views.index'),
        url(r'label/$','symcaptcha.views.submit_label_result'),
        url(r'rot/$','symcaptcha.views.index_rotate'),
        #url(r'/$','symcaptcha.views.'),
        )

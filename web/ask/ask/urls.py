from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import ask.views
import qa.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # /
    url(r'^$', qa.views.new, name='new'),
    # /login/
    url(r'^login/', ask.views.stub_ok, name='login'),
    # /signup/
    url(r'^signup/', ask.views.stub_ok, name='signup'),
    # /question/<123>/    # instead of <123> it must be a question_id
    url(r'^question/(?P<question_id>[0-9]+)/', qa.views.question_details, name='question_details'),
    # /ask/
    url(r'^ask/', ask.views.stub_ok, name='ask'),
    # /popular/
    url(r'^popular/', ask.views.stub_ok, name='popular'),
    # /admin/
    url(r'^admin/', include(admin.site.urls)),
)

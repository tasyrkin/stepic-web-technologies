from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import ask.views
import ask.urls_constants
import qa.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # /
    url(r'^$', qa.views.new, name=ask.urls_constants.NEW_URL_NAME),
    # /login/
    url(r'^login/', ask.views.stub_ok, name=ask.urls_constants.LOGIN_URL_NAME),
    # /signup/
    url(r'^signup/', ask.views.stub_ok, name=ask.urls_constants.SIGNUP_URL_NAME),
    # /question/<123>/    # instead of <123> it must be a question_id
    url(r'^question/(?P<question_id>[0-9]+)/', qa.views.question_details, name=ask.urls_constants.QUESTION_DETAILS_URL_NAME),
    # /ask/
    url(r'^ask/', ask.views.stub_ok, name=ask.urls_constants.ASK_URL_NAME),
    # /popular/
    url(r'^popular/', ask.views.stub_ok, name=ask.urls_constants.POPULAR_URL_NAME),
    # /admin/
    url(r'^admin/', include(admin.site.urls)),
)

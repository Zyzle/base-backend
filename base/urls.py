from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework.authtoken.views import obtain_auth_token

from views import home

urlpatterns = patterns('',
    url(r'^$', home),
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'snippets/', include('base.apps.snippets.urls', namespace="snippets")),
    url(r'^admin/', include(admin.site.urls)),
)

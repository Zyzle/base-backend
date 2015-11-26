from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

from views import home

urlpatterns = patterns('',
    url(r'^$', home),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'snippets/', include('base.apps.snippets.urls', namespace="snippets")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls'))
)

from django.conf.urls import url

from models import Snippet

from views import get_lexers, SnippetList, SnippetDetail

urlpatterns = [
    url(r'^lexers/$', get_lexers),
    url(r'^api/snippets/$', SnippetList.as_view()),
    url(r'^api/snippets/(?P<pk>\d+)/$', SnippetDetail.as_view())
]

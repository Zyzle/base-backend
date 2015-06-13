from django.http import JsonResponse

from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from models import Snippet
from serializers import SnippetListSerializer, SnippetDetailSerializer
from utils import lexers_list

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all();
    serializer_class = SnippetListSerializer
    autheitication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all();
    serializer_class = SnippetDetailSerializer
    autheitication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

def get_lexers(request):
    lexers = []

    for lexer, lexer_name in lexers_list():
        lexerMap = {}
        lexerMap["lexer"] = lexer
        lexerMap["name"] = lexer_name;
        lexers.append(lexerMap)

    return JsonResponse(lexers, content_type="application/json", safe=False)


from __future__ import print_function

from rest_framework import serializers

from models import Snippet

from utils import pygmentify

class SnippetListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Snippet
        fields = ("id", "title", "description", "snippet", "lexer_name", "usefulness")

    def create(self, validated_data):
        validated_data['snippet_html'] = pygmentify(validated_data['lexer_name'], validated_data['snippet'])
        return Snippet.objects.create(**validated_data)


class SnippetDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Snippet

    def update(self, instance, validated_data):
        validated_data['snippet_html'] = pygmentify(validated_data['lexer_name'], validated_data['snippet'])
        return serializers.ModelSerializer.update(self, instance, validated_data)



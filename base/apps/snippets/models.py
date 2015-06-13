from django.db import models

from utils import pygmentify, lexers_list

LEXER_CHOICES = lexers_list()

class Snippet(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    snippet = models.TextField()
    snippet_html = models.TextField(editable=False)
    lexer_name = models.CharField(max_length=255, choices=LEXER_CHOICES)
    usefulness = models.IntegerField(default=0)


    class Meta(object):
        ordering = ("-pub_date",)

    def __unicode__(self):
        return self.title

    def get_lexer(self):
        for lex in LEXER_CHOICES:
            if lex[0] == self.lexer_name:
                return lex[1]

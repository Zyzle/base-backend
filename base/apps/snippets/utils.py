from pygments import highlight
from pygments.lexers import get_lexer_by_name, get_all_lexers
from pygments.formatters import HtmlFormatter


def pygmentify(lexername, snippet):
    lexer = get_lexer_by_name(lexername, stripall=True)
    formatter = HtmlFormatter(linenos=True)
    return highlight(snippet, lexer, formatter)

def lexers_list():
    all_lex = [(x[1][0], x[0]) for x in get_all_lexers()]
    return sorted(all_lex, key=lambda name: name[1].lower())


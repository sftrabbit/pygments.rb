# -*- coding: utf-8 -*-
"""
    pygments.lexers.clang
    ~~~~~~~~~~~~~~~~~~~

    Custom lexer for Clang output
"""
import re

from pygments.lexer import RegexLexer, include, bygroups, \
    using, DelegatingLexer
from pygments.token import Text, Name, Number, String, Comment, Punctuation, \
     Other, Keyword, Operator, Literal, Whitespace

__all__ = ['ClangLexer']

class ClangLexer(RegexLexer):
    name = 'Clang'
    aliases = ['clang', 'Clang']
    filenames = []
    mimetypes = []

    tokens = {
        'root': [
            include('whitespace'),
            (r'^(error)(:[^\[$]*)', bygroups(Name.Tag, Text)),
            (r'^(warning)(:[^\[$]*)', bygroups(String, Text)),
            (r'^(note)(:[^\[$]*)', bygroups(Name.Function, Text)),
            (r'(\[.*?\])', bygroups(Comment.Single)),
            (r'.', Text),
        ],

        'whitespace': [
            (r'\n', Text),
            (r'[\r\n]+', Text),
            (r'\s+', Text),
        ],
    }

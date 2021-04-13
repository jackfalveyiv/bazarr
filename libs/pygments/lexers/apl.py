"""
    pygments.lexers.apl
    ~~~~~~~~~~~~~~~~~~~

    Lexers for APL.

    :copyright: Copyright 2006-2021 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from pygments.lexer import RegexLexer
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
    Number, Punctuation

__all__ = ['APLLexer']


class APLLexer(RegexLexer):
    """
    A simple `APL <https://en.m.wikipedia.org/wiki/APL_(programming_language)>`_ lexer.

    .. versionadded:: 2.0
    """
    name = 'APL'
    aliases = ['apl']
    filenames = ['*.apl']

    tokens = {
        'root': [
            # Whitespace
            # ==========
            (r'\s+', Text),
            #
            # Comment
            # =======
            # '⍝' is traditional; '#' is supported by GNU APL and NGN (but not Dyalog)
            (r'[⍝#].*$', Comment.Single),
            #
            # Strings
            # =======
            (r'\'((\'\')|[^\'])*\'', String.Single),
            (r'"(("")|[^"])*"', String.Double),  # supported by NGN APL
            #
            # Punctuation
            # ===========
            # This token type is used for diamond and parenthesis
            # but not for bracket and ; (see below)
            (r'[⋄◇()]', Punctuation),
            #
            # Array indexing
            # ==============
            # Since this token type is very important in APL, it is not included in
            # the punctuation token type but rather in the following one
            (r'[\[\];]', String.Regex),
            #
            # Distinguished names
            # ===================
            # following IBM APL2 standard
            (r'⎕[A-Za-zΔ∆⍙][A-Za-zΔ∆⍙_¯0-9]*', Name.Function),
            #
            # Labels
            # ======
            # following IBM APL2 standard
            # (r'[A-Za-zΔ∆⍙][A-Za-zΔ∆⍙_¯0-9]*:', Name.Label),
            #
            # Variables
            # =========
            # following IBM APL2 standard
            (r'[A-Za-zΔ∆⍙][A-Za-zΔ∆⍙_¯0-9]*', Name.Variable),
            #
            # Numbers
            # =======
            (r'¯?(0[Xx][0-9A-Fa-f]+|[0-9]*\.?[0-9]+([Ee][+¯]?[0-9]+)?|¯|∞)'
             r'([Jj]¯?(0[Xx][0-9A-Fa-f]+|[0-9]*\.?[0-9]+([Ee][+¯]?[0-9]+)?|¯|∞))?',
             Number),
            #
            # Operators
            # ==========
            (r'[\.\\\/⌿⍀¨⍣⍨⍠⍤∘⌸&⌶@⌺⍥⍛⍢]', Name.Attribute),  # closest token type
            (r'[+\-×÷⌈⌊∣|⍳?*⍟○!⌹<≤=>≥≠≡≢∊⍷∪∩~∨∧⍱⍲⍴,⍪⌽⊖⍉↑↓⊂⊃⌷⍋⍒⊤⊥⍕⍎⊣⊢⍁⍂≈⌸⍯↗⊆⊇⍸√⌾…⍮]',
             Operator),
            #
            # Constant
            # ========
            (r'⍬', Name.Constant),
            #
            # Quad symbol
            # ===========
            (r'[⎕⍞]', Name.Variable.Global),
            #
            # Arrows left/right
            # =================
            (r'[←→]', Keyword.Declaration),
            #
            # D-Fn
            # ====
            (r'[⍺⍵⍶⍹∇:]', Name.Builtin.Pseudo),
            (r'[{}]', Keyword.Type),
        ],
    }

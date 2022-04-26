import lexer as lexer
from sly import Parser

class c_WhereParser(Parser):
    tokens = lexer.b_Lexer.tokens

    @_('G_STRING_LITERAL G_STAR G_NUM_LITERAL')
    def expr(self, p):
        return p.G_STRING_LITERAL * p.G_NUM_LITERAL
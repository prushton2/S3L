import lexer as lexer
from sly import Parser
class w_Parser(Parser):
    # Get the token list from the lexer (required)
    tokens = lexer.b_Lexer.tokens
    # tokens = CalcLexer.tokens

    # Grammar rules and actions
    @_('expr G_STAR expr')
    def expr(self, p):
        return p.expr0 * p.expr1

    @_('G_STRING_LITERAL')
    def expr(self, p):
        return p.G_STRING_LITERAL[1:-1]

    @_('G_NUM_LITERAL')
    def expr(self, p):
        return int(p.G_NUM_LITERAL)


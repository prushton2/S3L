import lexer as lexer
from sly import Parser
import expressions as exp

class w_Parser(Parser):
    # Get the token list from the lexer (required)
    tokens = lexer.b_Lexer.tokens

    def __init__(self):
        self.checkList = []

    # tokens = CalcLexer.tokens

    # Grammar rules and actions
    @_('rawExpr G_STAR rawExpr')
    def rawExpr(self, p):
        print("Multiplying")
        return p.rawExpr0 * p.rawExpr1

    @_('G_STRING_LITERAL')
    def rawExpr(self, p):
        return p.G_STRING_LITERAL[1:-1]

    @_('G_NUM_LITERAL')
    def rawExpr(self, p):
        return int(p.G_NUM_LITERAL)

    @_('W_UNDERSCORE')
    def rawExpr(self, p):
        return p.W_UNDERSCORE
    
    @_('W_RANGE G_OPEN_PARENTHESIS rawExpr G_CLOSE_PARENTHESIS')
    def obj(self, p):
        return ""

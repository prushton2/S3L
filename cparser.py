import lexer as lexer
from sly import Parser
import expressions as exp

class w_Parser(Parser):
    # Get the token list from the lexer (required)
    tokens = lexer.b_Lexer.tokens

    def __init__(self):
        self.checkList = []

    precedence = (
        ('left', 'W_PLUS'),
        ('left', 'G_STAR')
    )

    # Grammar rules and actions

    @_('rawExpr W_PLUS rawExpr')
    def rawExpr(self, p):
        print(f"{p.rawExpr0} PLUS {p.rawExpr1}")
        return str(p.rawExpr0) + str(p.rawExpr1)
    
    @_('rawExpr G_STAR rawExpr')
    def rawExpr(self, p):
        print(f"{p.rawExpr0} STAR {p.rawExpr1}")
        return p.rawExpr0 * p.rawExpr1

    @_('G_STRING_LITERAL')
    def rawExpr(self, p):
        print("String literal -> rawExpr")
        return p.G_STRING_LITERAL[1:-1]

    @_('G_NUM_LITERAL')
    def rawExpr(self, p):
        print("Number literal -> rawExpr")
        return int(p.G_NUM_LITERAL)

    @_('W_UNDERSCORE')
    def rawExpr(self, p):
        print("Underscore -> rawExpr")
        return str(p.W_UNDERSCORE)

    @_('G_OPEN_PARENTHESIS rawExpr G_CLOSE_PARENTHESIS')
    def rawExpr(self, p):
        print("Parenthesis -> rawExpr")
        return p.rawExpr
        
    @_('W_RANGE rawExpr')
    def obj(self, p):
        print("Range -> obj")
        return 

# class s_Parser(Parser):
#     # Get the token list from the lexer (required)
#     tokens = lexer.b_Lexer.tokens

#     def __init__(self):
#         self.selectedCharacters = []

#     # tokens = CalcLexer.tokens

#     # Grammar rules and actions

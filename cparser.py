import lexer as lexer
from sly import Parser
import expressions as exp

# class s_Parser(Parser):
#     # Get the token list from the lexer (required)
#     tokens = lexer.b_Lexer.tokens

#     def __init__(self):
#         self.selectedCharacters = []

#     # tokens = CalcLexer.tokens

#     # Grammar rules and actions

class w_Parser(Parser):
    # Get the token list from the lexer (required)
    tokens = lexer.w_Lexer.tokens

    def __init__(self):
        self.objects = []

    precedence = (
        
        ('left', 'G_OPEN_PARENTHESIS'),

        ('left', 'W_UNDERSCORE', 'W_RANGE'),

        ('left', 'W_PLUS'),
        ('left', 'G_STAR'),

        ('left', 'G_STRING_LITERAL', 'G_NUM_LITERAL'),

    )

    # Grammar rules and actions

    @_('rawExpr W_PLUS rawExpr')
    def rawExpr(self, p):
        #print(f"{p.rawExpr0} PLUS {p.rawExpr1}")
        return str(p.rawExpr0) + str(p.rawExpr1)
    
    @_('rawExpr G_STAR rawExpr')
    def rawExpr(self, p):
        #print(f"{p.rawExpr0} STAR {p.rawExpr1}")
        return p.rawExpr0 * p.rawExpr1

    @_('G_STRING_LITERAL')
    def rawExpr(self, p):
        #print(f"String literal({p.G_STRING_LITERAL}) -> rawExpr")
        G_STRING_LITERAL = p.G_STRING_LITERAL
        if("&$" in p.G_STRING_LITERAL):
            index = p.G_STRING_LITERAL.find("&$")
            if (p.G_STRING_LITERAL[index-1] != "\\"):
                G_STRING_LITERAL = p.G_STRING_LITERAL[:index] + "\\" + p.G_STRING_LITERAL[index:]
        return G_STRING_LITERAL[1:-1]

    @_('G_NUM_LITERAL')
    def rawExpr(self, p):
        return int(p.G_NUM_LITERAL)


    @_('G_OPEN_PARENTHESIS rawExpr G_CLOSE_PARENTHESIS')
    def rawExpr(self, p):
        return p.rawExpr
        
    @_('W_UNDERSCORE')
    def rawExpr(self, p):
        index = len(self.objects)
        self.objects.append(exp.Underscore())
        return f"&${format(index, '4d')}"
    
    @_('W_RANGE G_OPEN_PARENTHESIS rawExpr G_CLOSE_PARENTHESIS')
    def rawExpr(self, p):
        index = len(self.objects)
        self.objects.append(exp.Range(p.rawExpr))
        return f"&${format(index, '4d')}"

class f_Parser(Parser):

    tokens = lexer.f_Lexer.tokens

    @_('G_STRING_LITERAL')
    def rawExpr(self, p):
        return p.G_STRING_LITERAL[1:-1]

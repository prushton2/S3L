import slyFiles.lexer as lexer
from sly import Parser
import expressions as exp

class s_Parser(Parser):
    # Get the token list from the lexer (required)
    tokens = lexer.s_Lexer.tokens

    def __init__(self):
        self.leftOutside = 0   #x<[] // Where x is the value stored in the variable
        self.rightOutside = 0  #[]>x
        self.leftInside = -1   #[>x] // -1 means that there was a * placed inside the brackets
        self.rightInside = -1  #[x<]
    
    @_('G_NUM_LITERAL S_LEFT_ARROW S_OPEN_BRACKET')
    def rawExpr(self, p):
        self.leftOutside = int(p.G_NUM_LITERAL)
        return p.S_OPEN_BRACKET

    @_('S_OPEN_BRACKET S_RIGHT_ARROW G_NUM_LITERAL')
    def rawExpr(self, p):
        self.leftInside = int(p.G_NUM_LITERAL)
        return p.S_OPEN_BRACKET

    @_('G_NUM_LITERAL S_LEFT_ARROW S_CLOSE_BRACKET')
    def rawExpr(self, p):
        self.rightInside = int(p.G_NUM_LITERAL)
        return p.S_CLOSE_BRACKET

    @_('S_CLOSE_BRACKET S_RIGHT_ARROW G_NUM_LITERAL')
    def rawExpr(self, p):
        self.rightOutside = int(p.G_NUM_LITERAL)
        return p.S_CLOSE_BRACKET
class w_Parser(Parser): 
    # This needs to be reworked. I parse everything here, and create a list of objects later. I can absolutely merge these
    # two functions into just the parser. This is going to reduce bugs and make it easier to read.
    # Get the token list from the lexer (required)
    tokens = lexer.w_Lexer.tokens

    def __init__(self):
        self.objects = []

    objectReferencePrefix = "&"

    precedence = (
        
        ('left', 'G_OPEN_PARENTHESIS'),

        ('left', 'W_UNDERSCORE', 'W_RANGE'),

        ('left', 'W_PLUS'),
        ('left', 'G_STAR'),

        ('left', 'G_STRING_LITERAL', 'G_NUM_LITERAL'),

    )

    def addObject(self, object):
        self.objects.append(object)
        index = len(self.objects)-1
        return f"{self.objectReferencePrefix}{format(index, '4d')}"

    # Grammar rules and actions

    @_('G_OPEN_PARENTHESIS rawExpr G_CLOSE_PARENTHESIS')
    def rawExpr(self, p):
        return p.rawExpr

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
        if(self.objectReferencePrefix in p.G_STRING_LITERAL):
            index = p.G_STRING_LITERAL.find(self.objectReferencePrefix)
            if (p.G_STRING_LITERAL[index-1] != "\\"):
                G_STRING_LITERAL = p.G_STRING_LITERAL[:index] + "\\" + p.G_STRING_LITERAL[index:]
        return G_STRING_LITERAL[1:-1]

    @_('G_NUM_LITERAL')
    def rawExpr(self, p):
        return int(p.G_NUM_LITERAL)

    @_('W_RANGE G_OPEN_PARENTHESIS rawExpr G_CLOSE_PARENTHESIS')
    def rawExpr(self, p):
        return self.addObject(exp.Range(p.rawExpr))

    @_('W_UNDERSCORE')
    def rawExpr(self, p):
        return self.addObject(exp.Underscore())
    
class f_Parser(Parser):

    tokens = lexer.f_Lexer.tokens

    @_('G_STRING_LITERAL')
    def rawExpr(self, p):
        return p.G_STRING_LITERAL[1:-1]

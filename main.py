from sly import Lexer
import command as cmd
import selectSyntax as SSyntax
import whereSyntax as WSyntax


class lexer(Lexer): # primary lexer
    tokens = {
        SELECT,
        FROM,
        WHERE,

        S_STAR,
        S_OPEN_BRACKET,
        S_CLOSE_BRACKET,

        W_STRING_LITERAL
    }
    
    # Base commands
    SELECT = cmd.select.regex
    FROM = cmd.from_.regex
    WHERE = cmd.where.regex
    
    # Select commands
    S_STAR = SSyntax.star.regex
    S_OPEN_BRACKET = SSyntax.openBracket.regex
    S_CLOSE_BRACKET = SSyntax.closeBracket.regex

    # Where commands
    W_STRING_LITERAL = WSyntax.stringLiteral.regex


    #this is important??
    ignore = r" \t"


while True:
    data = input("> ")
    for token in lexer().tokenize(data):
        print(token)
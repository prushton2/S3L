from sly import Lexer

import command      as cmd
import selectSyntax as SSyntax
import whereSyntax  as WSyntax
import globalSyntax as GSyntax

class lexer(Lexer): # primary lexer
    tokens = {
        B_SELECT,
        B_FROM,
        B_WHERE,

        S_STAR,
        S_OPEN_BRACKET,
        S_CLOSE_BRACKET,

        W_STR,

        G_STRING_LITERAL,
        G_SEMICOLON,

    }
    
    # Base commands
    B_SELECT = cmd.select.regex
    B_FROM = cmd.from_.regex
    B_WHERE = cmd.where.regex
    
    # Select commands
    S_STAR = SSyntax.star.regex
    S_OPEN_BRACKET = SSyntax.openBracket.regex
    S_CLOSE_BRACKET = SSyntax.closeBracket.regex

    # Where commands
    W_STR = WSyntax.str_.regex

    # Global commands
    G_STRING_LITERAL = GSyntax.stringLiteral.regex
    G_SEMICOLON = GSyntax.semicolon.regex


    #this is important??
    ignore = r" \t"


while True:
    data = input("> ")
    for token in lexer().tokenize(data):
        print(token)
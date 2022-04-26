from sly import Lexer, Parser

import command      as cmd
import selectSyntax as SSyntax
import whereSyntax  as WSyntax
import globalSyntax as GSyntax

class c_Lexer(Lexer): # primary lexer
    tokens = {
        B_SELECT,
        B_FROM,
        B_WHERE,
        B_SEMICOLON,

        S_OPEN_BRACKET,
        S_CLOSE_BRACKET,

        W_STR,
        W_PLUS,
        W_RANGE,

        G_STAR,
        G_STRING_LITERAL,
        G_NUM_LITERAL,
        G_OPEN_PARENTHESIS,
        G_CLOSE_PARENTHESIS,

    }
    
    # Base commands
    B_SELECT = cmd.select.regex
    B_FROM = cmd.from_.regex
    B_WHERE = cmd.where.regex
    B_SEMICOLON = cmd.semicolon.regex
    
    # Select commands
    S_OPEN_BRACKET = SSyntax.openBracket.regex
    S_CLOSE_BRACKET = SSyntax.closeBracket.regex

    # Where commands
    W_STR = WSyntax.str_.regex
    W_PLUS = WSyntax.plus.regex
    W_RANGE = WSyntax.range.regex

    # Global commands
    G_STAR = GSyntax.star.regex
    G_STRING_LITERAL = GSyntax.stringLiteral.regex
    G_NUM_LITERAL = GSyntax.numLiteral.regex
    G_OPEN_PARENTHESIS = GSyntax.openParenthesis.regex
    G_CLOSE_PARENTHESIS = GSyntax.closeParenthesis.regex


    #this is important??
    ignore = r" \t"


# class c_Parser(Parser):
#     tokens = c_Lexer.tokens

    


def splitTokens(tokens):
    splitTokens = {
        "B_SELECT": [],
        "B_WHERE": [],
        "B_FROM": []
    }

    mostRecentBaseTokenName = ""

    for token in tokens:
        
        # print(token)

        if(token.type == "B_SEMICOLON"):
            return splitTokens

        if(token.type[0] == "B"):
            mostRecentBaseTokenName = token.type
        else:
            splitTokens[mostRecentBaseTokenName].append(token)

    return splitTokens



def interpret(text):
    lexer = c_Lexer()
    # parser = c_Parser()

    tokens = lexer.tokenize(text)

    for token in tokens:
        print(token)

    if(False):
        tokens = splitTokens(tokens)
        print("),\n".join(str(tokens).split("),")))

    # result = parser.parse(tokens)


while True:
    interpret(input(">"))

#Stress test: select [*] where "e"*10+range("0-9") from "Heeeeeeeeee1 ayo"
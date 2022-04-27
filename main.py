import lexer as lexer
import cparser as parser

# There is absolutely a better way to do this. I'm just not sure how to do it. Either way, im learning about lexers, gimme a break.

def splitStatement(tokens):
    statementStrings = {
        "B_SELECT": "",
        "B_WHERE": "",
        "B_FROM": "",
        "": ""
    }

    mostRecentBaseTokenName = ""

    for token in tokens:

        if(token.type == "B_SEMICOLON"):
            break

        if(token.type[0] == "B"):
            mostRecentBaseTokenName = token.type
        else:
            statementStrings[mostRecentBaseTokenName] += (token.value)

    statementStrings = {
        "B_SELECT": statementStrings["B_SELECT"],
        "B_WHERE": statementStrings["B_WHERE"],
        "B_FROM": statementStrings["B_FROM"]
    }

    return statementStrings

def interpret(text):
    b_lexer = lexer.b_Lexer() #base lexer
    s_lexer = lexer.s_Lexer() #select lexer
    w_lexer = lexer.w_Lexer() #where lexer
    f_lexer = lexer.f_Lexer() #from lexer
    
    w_parser = parser.w_Parser()

    tokens = b_lexer.tokenize(text)

    statements = splitStatement(tokens)
    print(statements)

    selectTokens = s_lexer.tokenize(statements["B_SELECT"])
    whereTokens = w_lexer.tokenize(statements["B_WHERE"])
    fromTokens = f_lexer.tokenize(statements["B_FROM"])

    whereParse = w_parser.parse(whereTokens)
    print(whereParse)

while True:
    interpret(input(">"))

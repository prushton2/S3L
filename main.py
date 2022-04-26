import lexer as lexer
import cparser as parser


def splitTokens(tokens):
    splitTokens = {
        "B_SELECT": [],
        "B_WHERE": [],
        "B_FROM": []
    }

    mostRecentBaseTokenName = ""

    for token in tokens:
        
        # remove the '"' from the string literal
        if token.type == "G_STRING_LITERAL":
            token.value = token.value[1:-1]


        if(token.type == "B_SEMICOLON"):
            return splitTokens

        if(token.type[0] == "B"):
            mostRecentBaseTokenName = token.type
        else:
            splitTokens[mostRecentBaseTokenName].append(token)

    return splitTokens



def interpret(text):
    c_lexer = lexer.c_Lexer()
    c_WhereParser = parser.c_WhereParser()

    tokens = c_lexer.tokenize(text)

    print(tokens)
    # for token in tokens:
    #     print(token)

    tokens = splitTokens(tokens)
    print("),\n".join(str(tokens).split("),")))

    print(tokens["B_WHERE"])
    # selectParse = None
    whereParse = c_WhereParser.parse(tokens["B_WHERE"])

while True:
    interpret(input(">"))

#Stress test: select [*] where "e"*10+range("0-9") from "Heeeeeeeeee1 ayo"
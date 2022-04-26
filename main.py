from posixpath import split
import lexer as lexer
import cparser as parser

# There is absolutely a better way to do this. I'm just not sure how to do it. Either way, im learning about lexers, gimme a break.

def splitStatement(tokens):
    statementStrings = {
        "B_SELECT": "",
        "B_WHERE": "",
        "B_FROM": ""
    }

    mostRecentBaseTokenName = ""

    for token in tokens:

        if(token.type == "B_SEMICOLON"):
            break

        if(token.type[0] == "B"):
            mostRecentBaseTokenName = token.type
        else:
            statementStrings[mostRecentBaseTokenName] += (token.value+" ")

    statementStrings = {
        "B_SELECT": statementStrings["B_SELECT"][0:-1],
        "B_WHERE": statementStrings["B_WHERE"][0:-1],
        "B_FROM": statementStrings["B_FROM"][0:-1]
    }

    return statementStrings



def interpret(text):
    b_lexer = lexer.b_Lexer()
    s_lexer = lexer.s_Lexer()
    w_lexer = lexer.w_Lexer()
    f_lexer = lexer.f_Lexer()

    c_WhereParser = parser.c_WhereParser()



    tokens = b_lexer.tokenize(text)

    statements = splitStatement(tokens)
    print(statements)

    selectTokens = s_lexer.tokenize(statements["B_SELECT"])
    whereTokens = w_lexer.tokenize(statements["B_WHERE"])
    fromTokens = f_lexer.tokenize(statements["B_FROM"])

    print("---SELECT---")
    for i in selectTokens:
        print(i)

    print("---WHERE---")
    for i in whereTokens:
        print(i)

    print("---FROM---")
    for i in fromTokens:
        print(i)

while True:
    interpret(input(">"))

#Stress test: select [*] where "e"*10+range("0-9") from "Heeeeeeeeee1 ayo"
import slyFiles.lexer as lexer
import slyFiles.cparser as parser
import selector as selector

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
            if(mostRecentBaseTokenName == "B_SELECT"):
                if(token.type == "S_OPEN_BRACKET" or token.type == "S_CLOSE_BRACKET"):
                    statementStrings["B_SELECT"] += token.value+"_"
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
    
    s_parser = parser.s_Parser() #select parser
    w_parser = parser.w_Parser() #Where parser
    f_parser = parser.f_Parser() #Where parser

    tokens = b_lexer.tokenize(text)

    statements = splitStatement(tokens)

    print(statements)

    selectTokens = s_lexer.tokenize(statements["B_SELECT"])
    whereTokens = w_lexer.tokenize(statements["B_WHERE"])
    fromTokens = f_lexer.tokenize(statements["B_FROM"])

    selectParse = s_parser.parse(selectTokens)
    whereParse = w_parser.parse(whereTokens)
    fromParse = f_parser.parse(fromTokens)

    print(f"Parsed select clause: |{selectParse}|")
    print(f"Parsed where clause: |{whereParse}|")
    print(f"Parsed from clause: |{fromParse}|")
    extensionArray = [s_parser.leftOutside, s_parser.leftInside, s_parser.rightInside, s_parser.rightOutside]
    print(f"{s_parser.leftOutside}<[>{s_parser.leftInside}_{s_parser.rightInside}<]>{s_parser.rightOutside}")
    
    selection = selector.getMatchingIndices(whereParse, fromParse, w_parser.objects) #get indexes where the where clause matches the string
    print(f"Selection: {selection}")

    extension = selector.extendMatchingIndices(extensionArray, selection)
    print(f"Extension: {extension}")

    for index, char in enumerate(fromParse):
        printed = False

        for eIndex, eChar in enumerate(extension):
            if(eChar[0] <= index <= eChar[1]):
                if(not printed):
                    print('\033[4m' + char + '\033[0m', end='')
                    printed = True

        if(not printed):
            print(char, end='')
    print("")

def main():
    while True:
        interpret(input(">"))

if __name__ == "__main__":
    main()

import command as cmd

star = cmd.Command("*", r'\*')
stringLiteral = cmd.Command("string", r'"([^"\n]|(\\"))*"')
numLiteral = cmd.Command("num", r'\d+')

openParenthesis = cmd.Command("(", r'\(')
closeParenthesis = cmd.Command(")", r'\)')

# "e"*3+_"

# (?<=")([^"\n]|(\\"))*(?=")
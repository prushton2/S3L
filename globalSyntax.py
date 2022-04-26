import command as cmd

stringLiteral = cmd.Command("string", r'"([^;]*)"')
numLiteral = cmd.Command("num", r'\d+')
semicolon = cmd.Command(";", r'\;')
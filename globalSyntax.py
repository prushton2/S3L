import command as cmd

stringLiteral = cmd.Command("string", r'"([^;]*)"')
semicolon = cmd.Command(";", r'\;')
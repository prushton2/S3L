from sly import Lexer
import command as cmd

select = cmd.Command('select', [], r'SELECT')
from_ = cmd.Command('from', [], r'FROM')
where = cmd.Command('where', [], r'WHERE')

class lexer(Lexer): # primary lexer
    tokens = {
        SELECT,
        FROM,
        WHERE
    }
    
    SELECT = select.regex
    FROM = from_.regex
    WHERE = where.regex
    
    ignore = r" \t"


while True:
    data = input("> ")
    for token in lexer().tokenize(data):
        print(token)
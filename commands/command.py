class Command:
    def __init__(self, name, regex):
        self.name = name
        self.regex = regex

# Commands

select = Command('select', r'SELECT(?i)')
where = Command('where', r'WHERE(?i)')
from_ = Command('from', r'FROM(?i)')
semicolon = Command(";", r'\;')


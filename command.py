class Command:
    def __init__(self, name, regex):
        self.name = name
        self.regex = regex

# Commands

select = Command('select', r'SELECT(?i)')
from_ = Command('from', r'FROM(?i)')
where = Command('where', r'WHERE(?i)')
semicolon = Command(";", r'\;')


class Command:
    def __init__(self, name, regex):
        self.name = name
        self.regex = regex

# Commands

select = Command('select', r'SELECT')
from_ = Command('from', r'FROM')
where = Command('where', r'WHERE')

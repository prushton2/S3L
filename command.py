class Command:
    def __init__(self, name, subCommands, regex):
        self.name = name
        self.subCommands = subCommands
        self.regex = regex
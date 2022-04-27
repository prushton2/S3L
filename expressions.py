import re

class Check:
    def __init__(self, value):
        self.value = value

    def check(self, p):
        return self.value == p.value

class Range(Check):
    def __init__(self, value):
        super().__init__(value)

    def check(self, p):
        return re.match(f"{super().value}", p.value)

class Underscore(Check):
    def __init__(self):
        super().__init__(None)
        pass

    def check(self, p):
        return True

class StringLiteral(Check):
    def __init__(self, value):
        super().__init__(value)
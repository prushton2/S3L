import re

class Check:
    def __init__(self, value):
        self.value = value

    def check(self, p):
        return self.value == p.value
    
    def __str__(self):
        return f"Object: {self.value}"

    def matches(self, p):
        return self.value == p

class Literal(Check):
    def __init__(self, value):
        super().__init__(value)

    def __str__(self):
        return f"Literal: {self.value}"

class Range(Check):
    def __init__(self, value):
        super().__init__(value)

    def matches(self, p):
        return re.match(f"{super().value}", p.value)

class Underscore(Check):
    def __init__(self):
        super().__init__("_")
        pass

    def matches(self, p):
        return True
"""
module for storing programming languages.
Estimated time to complete: 1 hour
"""


class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        """store the name, typing, reflection and year of programming language"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Generates string for programming language"""
        return f"{self.name},{self.typing} Typing, Reflection = {self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determines if passed in langiage is dynamic"""
        return self.typing == "Dynamic"
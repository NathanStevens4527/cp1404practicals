"""   """
from prac_09.musician import Musician


class Band:
    """Represent a Band object."""

    def __init__(self, name="", members = []):
        """initialises a band object"""
        self.name = name
        self.members = []

    def __str__(self):
        return f"{self.members}"

    def add(self, member):
        """method for adding band member"""
        self.members.append(member)

    def play(self):
        for member in self.members:
            if len(member.instruments) == 0:
                print(f"{member.name} needs an instrument!")
            else:
                print(member)

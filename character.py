import random
from charsheet import getSheet


class Character:
    """Generate a character stat sheet for a given Name, Race, and Class.

    Returns:
        obj: Character
    """

    name = input("Name: ")
    race = input("Race: ")
    char_class = input("Class: ")
    strength = []
    dexterity = []
    constitution = []
    intelligence = []
    wisdom = []
    charisma = []

    def rollCharacter(self):
        """Roll a charcter sheet.

        Returns:
            dict: Character's stat sheet (STR, DEX, CON, INT, WIS, CHA)
        """
        attributes = [
            Character.strength,
            Character.dexterity,
            Character.constitution,
            Character.intelligence,
            Character.wisdom,
            Character.charisma,
        ]

        for i in range(1, 5):
            Character.strength.append(random.randint(1, 6))
            Character.dexterity.append(random.randint(1, 6))
            Character.constitution.append(random.randint(1, 6))
            Character.intelligence.append(random.randint(1, 6))
            Character.wisdom.append(random.randint(1, 6))
            Character.charisma.append(random.randint(1, 6))

        for attribute in attributes:
            attribute.sort()
            del attribute[0]

        self.STR = str(sum(attributes[0]))
        self.DEX = str(sum(attributes[1]))
        self.CON = str(sum(attributes[2]))
        self.INT = str(sum(attributes[3]))
        self.WIS = str(sum(attributes[4]))
        self.CHA = str(sum(attributes[5]))
        self.stats = {
            "STR": self.STR,
            "DEX": self.DEX,
            "CON": self.CON,
            "INT": self.INT,
            "WIS": self.WIS,
            "CHA": self.CHA,
        }
        return self.stats


def main():
    char.rollCharacter()
    sheet = (
        "NAME: " + char.name,
        "RACE: " + char.race,
        "CLASS: " + char.char_class,
        char.stats,
    )
    getSheet(CHARACTER, sheet)


char = Character()
CHARACTER = char.name

main()

import random
from pprint import pprint

class Character():
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
        attributes = [Character.strength, Character.dexterity, Character.constitution, Character.intelligence, Character.wisdom, Character.charisma]

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
        self.stats = {"STR": self.STR, "DEX": self.DEX, "CON": self.CON, "INT": self.INT, "WIS": self.WIS, "CHA": self.CHA}
        return self.stats

def writeOut(sheet):
    file = open('/home/logank/projects/pf/characters/' + (str(Character.name + '.txt')), 'w')
    file.write(str(sheet))
    file.close()

def main():
    char = Character()
    char.rollCharacter()
    sheet = (char.name, char.race, char.char_class, char.stats)
    writeOut(sheet)

main()

# pprint(sheet, indent=4, compact=True, sort_dicts=False)
# Prints outpup to terminal

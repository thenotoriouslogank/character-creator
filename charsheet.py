import json


def getSheet(CHARACTER, sheet):
    """Write a .json formatted character sheet.

    Args:
        CHARACTER (str): Name of the character; used as output filename (./characters/[CHARACTER].json)
        sheet (tuple): Character stat sheet (see character.py for more info)
    """
    json_string = json.dumps(sheet, indent=2)
    with open("./characters/" + str(CHARACTER) + ".json", "w") as f:
        f.write(json_string)
        f.close()

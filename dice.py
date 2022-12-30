import argparse
import random

parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    description="Rolls (x) number of n-sided dice.",
)
parser.add_argument(
    "-L", "--droplowest", type=int, help="Drop lowest (x) number of rolls."
)
parser.add_argument(
    "-H", "--drophighest", type=int, help="Drop highest (x) number of rolls."
)
parser.add_argument("-s", "--sum", action="store_true", help="Sum total of rolls.")
parser.add_argument(
    "-n", "--natural", action="store_true", help="Only show results of natural 20 or 1."
)
args = parser.parse_args()

xdy = input("What would you like to roll? [xdy] ")
d = xdy.find("d")
amount = int(xdy[0:d])
sides = int(xdy[d + 1 :])


def roll(amount, sides):
    """Roll (x) number of (y)-sided dice.

    Args:
        amount (int): Number of dice to roll.
        sides (int): Specific die to roll.
    """
    rolls = []
    for i in range(0, amount):
        rolls.append(random.randint(1, sides))
    if args.natural:
        if max(rolls) == 20:
            print("CRITICAL SUCCESS!")
        elif min(rolls) == 1:
            print("CRITICAL FAILURE!")
        else:
            print(rolls)
    elif args.sum:
        print(sum(rolls))
    elif args.drophighest:
        print("Dropping highest " + str(args.drophighest) + " roll(s).")
        rolls.sort()
        del rolls[-(args.drophighest) :]
        print(rolls)
    elif args.droplowest:
        print("Dropping lowest " + str(args.droplowest) + " rolls(s).")
        rolls.sort()
        del rolls[0 : (args.droplowest)]
        print(rolls)
    else:
        print(rolls)


def main():
    (roll(amount, sides))

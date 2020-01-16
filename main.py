import pprint

from dice import roll
from lib.racelib import Human
from lib.classlib import Fighter
from lib.backgroundlib import Acolyte
from random import choice


def main():
    s = []

    for x in range(0, 6):
        r = roll('4d6')
        r.remove(min(r))
        s.append(sum(r))

    s = sorted(s, reverse=True)

    # Some attributes are prioritized differently for different classes.
    char_race = choice([Human()])
    char_class = choice([Fighter(s[0], s[1], s[2], s[3], s[4], s[5])])
    char_background = choice([Acolyte()])

    pp = pprint.PrettyPrinter(indent=4)

    pp.pprint(vars(char_class))


if __name__ == "__main__":
    main()

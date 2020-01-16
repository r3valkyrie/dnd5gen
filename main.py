import pprint
from random import choice

from dice import roll

from lib.backgroundlib import Acolyte
from lib.classlib import Fighter
from lib.racelib import Human


class Character:
    def __init__(self):
        a = []

        for x in range(0, 6):
            r = roll('4d6')
            r.remove(min(r))
            a.append(sum(r))

        a = sorted(a, reverse=True)

        # Some attributes are prioritized differently for different classes.
        char_background = choice([Acolyte()])
        char_race = choice([Human(char_background)])
        char_class = choice(
            [Fighter(a[0], a[1], a[2], a[3], a[4], a[5], char_race, char_background)])

        # Character info
        self.name = char_race.full_name
        self.race = char_race.race
        self.gender = char_race.gender
        self.hair_color = char_race.hair_color
        self.alignment = f'{choice(["Lawful", "Neutral", "Chaotic"])} ' \
                         f'{choice(["Good", "Neutral", "Evil"])}'
        if self.alignment == "Neutral Neutral":
            self.alignment = "Neutral"
        self.speed = 30
        self.languages = char_race.languages_known
        self.background = char_background.background_name

        # Ability scores
        self.strength = char_class.as_scores[0]
        self.strength_mod = char_class.as_mods[0]
        self.dexterity = char_class.as_scores[1]
        self.dexterity_mod = char_class.as_mods[1]
        self.constitution = char_class.as_scores[2]
        self.constitution_mod = char_class.as_mods[2]
        self.intelligence = char_class.as_scores[3]
        self.intelligence_mod = char_class.as_mods[3]
        self.wisdom = char_class.as_scores[4]
        self.wisdom_mod = char_class.as_mods[4]
        self.charisma = char_class.as_scores[5]
        self.charisma_mod = char_class.as_mods[5]

        # Class info
        self.classname = char_class.classname
        self.level = char_class.level
        self.hp = char_class.hit_points
        self.armor_profs = char_class.armor_profs
        self.weapon_profs = char_class.weapon_profs
        self.tool_profs = char_class.tool_profs
        self.saving_throws = char_class.saving_throws
        self.skills = char_class.skills
        self.equipment = char_background.equipment + char_class.equipment
        self.features = char_background.features + char_race.features + char_class.features

        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(vars(self))


if __name__ == "__main__":
    Character()

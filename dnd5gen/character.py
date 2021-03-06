try:
    from inspect import getmembers, isclass
    from random import choice, randrange

except ImportError:
    from random import choice, randrange

    raise ImportError

finally:
    import dnd5gen.char_backgrounds as bgs
    import dnd5gen.char_races as races
    import dnd5gen.char_classes as classes


class Character:
    def __init__(self, level=None):

        # Generate ability scores
        a = []
        for x in range(0, 6):
            r = []
            for y in range(0, 4):
                r.append(randrange(1, 7))
            r.remove(min(r))
            a.append(sum(r))

        a = sorted(a, reverse=True)

        # Check if a level was specified
        self.level = randrange(1, 21) if level is None else level

        # Some attributes are prioritized differently for different classes.

        char_background = choice(getmembers(bgs, isclass))[1]()
        char_race = choice(getmembers(races, isclass))[1](char_background)
        char_class = choice(
            [classes.Fighter(a[0], a[1], a[2], a[3], a[4], a[5],
                             char_race,
                             char_background,
                             self.level)])

        # Character info
        self.name = char_race.full_name
        self.race = char_race.race
        self.gender = char_race.gender
        self.hair_color = char_race.hair_color
        self.alignment = f'{choice(["Lawful", "Neutral", "Chaotic"])} ' \
                         f'{choice(["Good", "Neutral", "Evil"])}'
        if self.alignment == "Neutral Neutral":
            self.alignment = "Neutral"
        self.speed = char_race.speed
        self.size = char_race.size
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
        self.hp = char_class.hp
        self.armor_profs = char_class.armor_profs
        self.weapon_profs = char_class.weapon_profs
        self.tool_profs = char_class.tool_profs
        self.saving_throws = char_class.saving_throws
        self.skills = char_class.skills
        self.equipment = char_background.equipment + char_class.equipment
        self.features = char_background.features + char_race.features + char_class.features

    def print_char_vals(self):
        hr = "-" * 35
        nl = '\n'
        sm = "-" * 5
        out_str = f"""

{hr}
Name: {self.name}
Class: {self.classname} {self.level}
Race: {self.race}
Alignment: {self.alignment}
Background: {self.background}
{hr}
STR: {self.strength:2}({self.strength_mod:2}) DEX: {self.dexterity:2}({self.dexterity_mod:2}) CON: {self.constitution:2}({self.constitution_mod:2})
INT: {self.intelligence:2}({self.intelligence_mod:2}) WIS: {self.wisdom:2}({self.wisdom_mod:2}) CHA: {self.charisma:2}({self.charisma_mod:2})
{hr}
SKILL PROFICIENCIES\n
{nl.join(self.skills)}
{hr}
LANGUAGES\n
{nl.join(self.languages)}
{hr}
ARMOR PROFICIENCIES\n
{nl.join(self.armor_profs)}
{hr}
WEAPON PROFICIENCIES\n
{nl.join(self.weapon_profs)}
{hr}
TOOL PROFICIENCIES\n
{nl.join(self.tool_profs)}
{hr}
EQUIPMENT\n
{nl.join(self.equipment)}
{hr}
FEATURES
"""
        print(out_str)
        for x in self.features:
            print(f"""{x[0]}
{sm}
{x[1]}
{nl}
""")


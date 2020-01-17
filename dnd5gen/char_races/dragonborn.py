try:
    from random import choice, randrange, sample
    from os import path
    from json import load
except ImportError:
    raise ImportError


class Dragonborn:
    def __init__(self, char_background):
        self.race = "Dragonborn"
        self.gender = choice(['male', 'female', 'other'])
        self.bonus_asi = [2, 0, 0, 0, 0, 1]

        resource_path = path.join(path.dirname(__file__))
        with open(resource_path + "/../resources/names_dragonborn.json") as dragonborn_names:
            names = load(dragonborn_names)
            self.first_name = choice(names['clan'])
            if self.gender != 'other':
                self.last_name = choice(names[self.gender])
            else:
                self.last_name = choice(names[choice(['male', 'female'])])

        self.full_name = f"{self.first_name} {self.last_name}"
        self.hair_color = "None"
        self.skin_color = choice(["Black", "Blue", "Brass", "Bronze", "Copper",
                                  "Gold", "Green", "Red", "Silver", "White"])
        self.age = randrange(15, 60)
        self.speed = 30
        self.size = 'Medium'
        with open(resource_path + "/../resources/languages.json") as languages:
            langs = load(languages)
            for x in ["Common", "Draconic"]:
                langs.remove(x)
        self.languages_known = ["Common", "Draconic"] + \
            [x for x in sample(langs, 1 + char_background.add_langs)]
        self.ancestry = {
            "Black": ['Acid', '5 by 30 ft. line (Dex save)'],
            "Blue": ['Lightning', '5 by 30 ft. line (Dex save)'],
            "Brass": ['Fire', '5 by 30 ft. line (Dex save)'],
            "Bronze": ['Lightning', '5 by 30 ft. line (Dex save)'],
            "Copper": ['Acid', '5 by 30 ft. line (Dex save)'],
            "Gold": ['Fire', '15 ft. cone (Dex save)'],
            "Green": ['Poison', '15 ft. cone (Con save)'],
            "Red": ['Fire', '15 ft. cone (Dex save)'],
            "Silver": ['Cold', '15 ft. cone (Con save)'],
            "White": ['Cold', '15 ft. cone (Con save)'],
        }
        self.features = [["Breath Weapon",
                          "You can use your action to exhale destructive energy. Your "
                          "draconic ancestry determines the size, shape, and damage type "
                          "of the exhalation. When you use your breath weapon, each creature "
                          "in the area of the exhalation must make a saving throw, the type "
                          "of which is determined by your draconic ancestry. The DC for this "
                          "saving throw equals 8 + your Constitution modifier + your "
                          "proficiency bonus. A creature takes 2d6 damage on a failed save, "
                          "and half as much damage on a successful one. The damage "
                          "increases to 3d6 at 6th level, 4d6 at 11th level, and 5d6 at "
                          "16th level. After you use your breath weapon, you can’t use "
                          "it again until you complete a short or long rest."
                          ""
                          f"\nYou deal {self.ancestry[self.skin_color][0]} damage in a "
                          f"{self.ancestry[self.skin_color][1]}."]]
        self.features.append(["Damage Resistance",
                              f"You have resistance to {self.ancestry[self.skin_color][0]} damage."])

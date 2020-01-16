"""
Returns a race object.
"""
from os import path
from json import load
from random import choice, randrange, sample


class Human:
    def __init__(self, char_background):
        resource_path = path.join(path.dirname(__file__))
        with open(resource_path + "/resources/names_human.json") as human_names:
            names = load(human_names)

        with open(resource_path + "/resources/languages.json") as languages:
            langs = load(languages)
            langs.remove("Common")

        self.race = "Human"
        self.gender = choice(['male', 'female'])
        self.first_name = choice(names['first'][self.gender])
        self.last_name = choice(names['last'])
        self.full_name = f"{self.first_name} {self.last_name}"
        self.hair_color = choice(["Blonde", "Ginger", "Burgandy", "Honey",
                                  "Light Brown", "Brown", "Dark Brown", "Black"])
        self.skin_color = choice(["Fair", "Light", "Medium", "Olive",
                                  "Tan", "Brown", "Dark Brown", "Black"])
        self.age = randrange(18, 60)
        self.speed = 30
        self.languages_known = ["Common"] + \
                               [x for x in sample(langs, 1 + char_background.add_langs)]
        self.features = []

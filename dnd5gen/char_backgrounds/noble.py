from random import choice
from os import path
from json import load


class Noble:
    def __init__(self):
        self.background_name = "Noble"
        self.skill_profs = ["History", "Persuasion"]
        resource_path = path.join(path.dirname(__file__))
        with open(resource_path + '/../resources/items.json') as items:
            tools_gaming = load(items)['tools']['gaming']
            self.tool_profs = [choice(tools_gaming)]
        self.add_langs = 1
        self.equipment = ["Fine clothes", "Signet ring", "Scroll of pedigree",
                          "Purse containing 25 GP"]
        self.features = [['Position of Privilege',
                          "Thanks to your noble birth, people are inclined to think "
                          "the best of you. You are welcome in high society, and people "
                          "assume you have the right to be wherever you are. The common "
                          "folk make every effort to accommodate you and avoid your "
                          "displeasure, and other people of high birth treat you as a "
                          "member of the same social sphere. You can secure an audience "
                          "with a local noble if you need to."]]

from random import choice
from os import path
from json import load


class FolkHero:
    def __init__(self):
        self.background_name = "Folk Hero"
        self.skill_profs = ["Animal Handling", "Survival"]
        resource_path = path.join(path.dirname(__file__))
        with open(resource_path + '/../resources/items.json') as items:
            tools_artisan = load(items)['tools']['artisan']
            self.tool_profs = [choice(tools_artisan), "Vehicles (land)"]
        self.add_langs = 0
        self.equipment = [self.tool_profs[0], "Shovel", "Iron Pot", "Common Clothes",
                          "Pouch containing 10 gp"]
        self.features = [['Rustic Hospitality', 'Since you come from the ranks of the '
                                                'common folk, you fit in among them with ease. '
                                                'You can find a place to hide, rest, or recuperate '
                                                'among other commoners, unless you have shown '
                                                'yourself to be a danger to them. They will '
                                                'shield you from the law or anyone else searching '
                                                'for you, though they will not risk their lives '
                                                'for you.']]

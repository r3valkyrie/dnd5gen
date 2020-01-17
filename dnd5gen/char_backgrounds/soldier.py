from random import choice
from os import path
from json import load


class Soldier:
    def __init__(self):
        self.background_name = "Soldier"
        self.skill_profs = ["Athletics", "Intimidation"]
        resource_path = path.join(path.dirname(__file__))
        with open(resource_path + '/../resources/items.json') as items:
            tools_gaming = load(items)['tools']['gaming']
            self.tool_profs = [choice(tools_gaming), "Vehicles (land)"]
        self.add_langs = 0
        self.equipment = [self.tool_profs[0], "Insignia of rank",
                          choice(["Dagger", "Broken blade", "Piece of a banner"]),
                          "Common clothes", "Pouch containing 10 gp"]
        self.features = [["Military Rank",
                          "You have a military rank from your career as a soldier. "
                          "Soldiers loyal to your former military organization still "
                          "recognize your authority and influence, and they defer to you "
                          "if they are of a lower rank. You can invoke your rank to exert "
                          "influence over other soldiers and requisition simple equipment "
                          "or horses for temporary use. You can also usually gain access to "
                          "friendly military encampments and fortresses where your rank "
                          "is recognized."]]

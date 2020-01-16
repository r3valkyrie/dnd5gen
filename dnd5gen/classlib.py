"""
Returns a character_class object.
"""
from os import path
from json import load
from math import floor
from random import choice, sample


def get_as_mod(as_value):
    return floor((as_value - 10) / 2)


class Fighter:
    def __init__(self, as_str, as_dex, as_con,
                 as_int, as_wis, as_cha, char_race, char_background):
        self.classname = "Fighter"
        self.as_scores = [as_str, as_dex, as_con, as_int, as_wis, as_cha]
        self.as_mods = []
        for x in [as_str, as_dex, as_con, as_int, as_wis, as_cha]:
            self.as_mods.append(get_as_mod(x))
        self.level = 1
        self.hit_points = 10 + self.as_mods[2]
        self.armor_profs = [
            "Heavy armor",
            "Medium armor",
            "Light armor",
            "Shields",
        ]
        self.weapon_profs = [
            "Simple weapons",
            "Martial weapons"
        ]
        self.tool_profs = []
        self.saving_throws = ["str", "con"]
        self.skills = []
        self.equipment = []
        resource_path = path.join(path.dirname(__file__))
        with open(resource_path + '/resources/items.json') as items:
            martial_weapon = load(items)['weapons']['martial']
            equipment_choices = [
                # Equipment A
                [["Chain mail"],
                 ["Leather armor", "Longbow", "20 arrows"]],
                # Equipment B
                [[choice(martial_weapon), "Shield"],
                 [choice(martial_weapon), choice(martial_weapon)]],
                # Equipment C
                [["Light crossbow", "20 bolts"],
                 ["Handaxe", "Handaxe"]],
                # Equipment D
                [["Dungeoneer's pack"],
                 ["Explorer's pack"]]
            ]
            for x in equipment_choices:
                for y in choice(x):
                    self.equipment.append(y)

        skill_choices = ["Acrobatics", "Animal Handling", "Athletics",
                         "History", "Insight", "Intimidation", "Perception", "Survival"]
        for x in char_background.add_skills:
            if x in skill_choices:
                skill_choices.remove(x)

        self.skills = char_background.add_skills + sample(skill_choices, 2)
        self.features = [[
            "Second Wind",
            "You have a limited well of stamina that you can draw on to protect yourself "
            "from harm. On your turn, you can use a bonus action to regain hit points equal "
            "to 1d10 + your fighter level. Once you use this feature, you must finish a short "
            "or long rest before you can use it again"
        ]]
        fighting_styles = [
            ["Archery", "You gain a +2 bonus to attack rolls you make with ranged weapons."],
            ["Defense", "While you are wearing armor, you gain a +1 bonus to AC."],
            ["Dueling", "When you are wielding a melee weapon in one hand an no other weapons,"
                        " you gain a +2 bonus to damage rolls with that weapon."],
            ["Great Weapon Fighting", "When you roll a 1 or 2 on a damage die for an attack you"
                                      " make with a melee weapon that you are wielding with two"
                                      " hands, you can reroll the die and must use the new roll,"
                                      " even if the new roll is a 1 or a 2. The weapon must have"
                                      " the two-handed or versatile property for you to gain"
                                      " this benefit."]
        ]
        self.features.append(choice(fighting_styles))

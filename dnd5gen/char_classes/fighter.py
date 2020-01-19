try:
    from json import load
    from math import floor
    from os import path
    from random import choice, sample, randrange
except ImportError:
    raise ImportError


class Fighter:
    def __init__(self, as_str, as_con, as_dex,
                 as_int, as_wis, as_cha, char_race, char_background, level):
        self.classname = "Fighter"
        self.level = level
        self.subclass = ""
        self.as_scores = []

        for x, y in zip(char_race.bonus_asi, [as_str, as_dex, as_con, as_int, as_wis, as_cha]):
            self.as_scores.append(x + y)

        # Handle ASIs after level ups.
        asi_points = 0
        for x in [4, 6, 8, 12, 14, 16, 19]:
            if self.level >= x:
                asi_points += 2

        for x in range(0, 6):
            while self.as_scores[x] < 20 and asi_points > 0:
                self.as_scores[x] += 1
                asi_points -= 1

        self.as_mods = []
        for x in self.as_scores:
            self.as_mods.append(floor((x - 10) / 2))
        self.hp = (10 + self.as_mods[2]) + sum([randrange(1, 11) for x in range(0,
                                                                                self.level - 1)])

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
        for x in char_background.tool_profs:
            self.tool_profs.append(x)
        self.saving_throws = ["Strength", "Constitution"]
        self.equipment = []
        resource_path = path.join(path.dirname(__file__))
        with open(resource_path + '/../resources/items.json') as items:
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

        self.skills = []
        skill_choices = ["Acrobatics", "Animal Handling", "Athletics",
                         "History", "Insight", "Intimidation", "Perception", "Survival"]
        for x in char_background.skill_profs:
            if x in skill_choices:
                skill_choices.remove(x)

        self.skills = char_background.skill_profs + sample(skill_choices, 2)
        self.features = []

        self.fighting_styles = [
            ["Archery",
             "You gain a +2 bonus to attack rolls you make with ranged weapons."],
            ["Defense",
             "While you are wearing armor, you gain a +1 bonus to AC."],
            ["Dueling",
             "When you are wielding a melee weapon in one hand and no other weapons, "
             "you gain a +2 bonus to damage rolls with that weapon."],
            ["Great Weapon Fighting",
             "When you roll a 1 or 2 on a damage die for an attack you make with a melee "
             "weapon that you are wielding with two hands, you can reroll the die and must "
             "use the new roll, even if the new roll is a 1 or a 2. The weapon must have "
             "the two-handed or versatile property for you to gain this benefit."],
            ["Protection",
             "When a creature you can see attacks a target other than you that is within "
             "5 feet of you, you can use your reaction to impose disadvantage on the attack "
             "roll. You must be wielding a shield."],
            ["Two-Weapon Fighting",
             "When you engage in two-weapon fighting, you can add your ability modifier to "
             "the damage of the second attack."]
        ]

        y = choice(self.fighting_styles)
        self.features.append(y)
        # Can't pick the same fighting style more than once.
        self.fighting_styles.remove(y)

        if self.level >= 3:
            choice([self.subclass_champion()])

        fighter_feats = {
            2: ["Action Surge",
                "Starting at 2nd level, you can push yourself beyond your normal limits for a "
                "moment. On your turn, you can take one additional action. Once you use this "
                "feature, you must finish a short or long rest before you can use it again. "
                "Starting at 17th level, you can use it twice before a rest, but only once "
                "on the same turn."],
            5: ["Extra Attack",
                "Beginning at 5th level, you can attack twice, instead of once, whenever "
                "you take the Attack action on your turn. The number of attacks increases to "
                "three when you reach 11th level in this class and to four when you reach 20th "
                "level in this class."],
            9: ["Indomitable",
                "Beginning at 9th level, you can reroll a saving throw that you fail. If you "
                "do so, you must use the new roll, and you can’t use this feature again until "
                "you finish a long rest. You can use this feature twice between long rests "
                "starting at 13th level and three times between long rests starting at 17th "
                "level."],
        }

        for x in fighter_feats:
            if self.level >= x:
                self.features.append(fighter_feats[x])

    def subclass_champion(self):
        self.subclass = "Champion"

        subclass_feats = {
            3: ["Improved Critical",
                "Beginning when you choose this archetype at 3rd level, "
                "your " "weapon attacks score a critical hit on a roll "
                "of 19 or 20."],
            7: ["Remarkable Athlete",
                "Starting at 7th level, you can add half your proficiency "
                "bonus (round up) to any Strength, Dexterity, or Constitution "
                "check you make that doesn’t already use your proficiency "
                "bonus. In addition, when you make a running long jump, the "
                "distance you can cover increases by a number of feet equal "
                "to your Strength modifier."],
            # TODO: Implement this functionality
            10: choice(self.fighting_styles),
            15: ["Superior Critical",
                 "Starting at 15th level, your weapon attacks score a critical hit "
                 "on a roll of 18–20."],
            18: ["Survivor",
                 "At 18th level, you attain the pinnacle of resilience in battle. "
                 "At the start of each of your turns, you regain hit points equal "
                 "to 5 + your Constitution modifier if you have no more than half of "
                 "your hit points left. You don’t gain this benefit if you have 0 hit points."]
        }

        for x in subclass_feats:
            if self.level >= x:
                self.features.append(subclass_feats[x])

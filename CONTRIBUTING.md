
# Contributing
The backgrounds, races, and classes are all modular, and should all work without
needing to edit any of the main files assuming they all return the proper
attributes.

Please ensure that all non-python files are placed in `dnd5gen/resources` so that they get picked
up by setuptools during build time.

### Adding backgrounds
Create a new python class in `dnd5gen/char_backgrounds/`. The class should
take no arguments (except `self`), and should have all of the following attributes set after
initialization. After creation, import the class in `dnd5gen/char_backgrounds/__init__.py`.
```python
class BgName:
    def __init__(self):
        # str containing the name of the background.
        self.background_name = "BgName"
        
        # list of str containing all proficiencies granted by the background.
        self.skill_profs = ["Proficiency 1", "Proficiency 2"]

        # list of str containing all tool proficiencies granted by the background.
        self.tool_profs = ["Tool 1", "Tool 2"]

        # int representing the additional language choices you are given (handled by char_classes)
        self.add_langs = 1

        # list of str containing the equipment granted by your background.
        self.equipment = ["Robe", "Wizard Hat"]

        # list of lists of str containing any features granted by your background.
        self.features = [["Putting It On", 
                        "You are adept at putting on your robe and wizard hat."]]
```

### Adding Races
Create a new python class in `dnd5gen/char_races/`. The class should take
 two arguments, `self` and `char_background`, and should have all of the following attributes set
 after initialization. After creation, import the class in `dnd5gen/char_races/__init__.py`.
 
```python
try:
    from random import choice, randrange, sample
    from os import path
    from json import load
except ImportError:
    raise ImportError

class RaceName:
    def __init__(self, char_background):
        # str containing the name of the race.
        self.race = "RaceName"
        
        # str containing the chosen gender.
        self.gender = choice(['male', 'female', 'other'])

        # list of 6 integers representing the racial ASIs.
        # here, they are ordered by STR, DEX, CON, INT, WIS, CHA
        self.bonus_asi = [1, 1, 0, 0, 2, 0]

        # str containing the character's full name.
        # Different races might have varying naming schemes. This library doesn't care how you
        # generate them as long as this attribute is correctly filled.
        self.full_name = choice(["Barnabus Bimblewhiz", "Joe Schmoe", "Sally Sue"])

        # str containing the character's hair color.
        self.hair_color = choice(["Blonde", "Blue", "Black"])

        # str containing the character's skin color.
        self.skin_color = choice(["Fair", "Medium", "Tan", "Brown", "Black"])

        # int containing the character's age. Different races have different lifespans.
        self.age = randrange(18,550)

        # int containing the character's speed. Different races have different base speeds.
        self.speed = 30

        # str containing the race's size.
        self.size = 'Medium'


        # list of str containing the character's known languages.
        # Avoid having duplicate languages in the list, since you can't know the same language twice.
        resource_path = path.join(path.dirname(__file__))
        with open (resource_path + "/../resources/languages.json") as languages:
            langs = load(languages)
            # The race knows common already
            langs.remove("Common")
            self.languages_known = ["Common"] + \
                                    [x for x in sample(langs, 1 + char_background.add_langs)]

        # list of lists of str containing any racial features.
        self.features = [["Big Feature",
                            "Thanks to your heritage, you can do a thing."]]
```

### Adding Classes
Create a new python file in `dnd5gen/char_classes/` and create a class to represent the character
class. The class takes the following arguments:
```python
class CharacterClass:
    def __init__(self, AS1, AS2, AS3, AS4, AS5, AS6, char_race, char_background, level):
        pass
```

Remember that ability scores are passed to the class's arguments in order of highest to lowest.
Because of this, you should prioritize a class's primary stats first. Take the
rogue for example. You would likely want AS1 to be DexGithub Darkterity, followed by Charisma for AS2, 
followed by the other stats.

Most of the final ability score calculations are handled here, so you want to pass the character's
race to include any racial ASIs.

Once the class is created, import it into `dnd5gen/char_classes/__init__.py`.

```python
# I'm using the rogue for demonstration purposes.
try:
    from math import floor
    from os import path
    from random import choice, sample, randrange
except ImportError:
    raise ImportError

class Rogue:
    def __init__(self, as_dex, as_cha, as_con,
                 as_int, as_wis, as_str,
                 char_race, char_background, level):
        # str containing the class's name.
        self.classname = "Rogue"

        # str containing the subclass, should be empty by default.
        self.subclass = ""

        # int containing the level, passed from args.
        self.level = level

        # list of int containing the ability scores. You want to include the bonus ASIs
        # from your race. This is one way to do it.
        self.as_scores = []
        
        # These should always be ordered as normal.
        # STR DEX CON INT WIS CHA
        for x,y in zip(char_race.bonus_asi, [as_str, as_dex, as_con, as_int, as_wis, as_cha]):
            self.as_scores.append(x + y)

        # You get ASIs when you reach certain levels in a class. Make sure those get calculated.
        asi_points = 0
        for x in [4, 8, 10, 12, 16, 19]:
            if self.level >= x:
                asi_points += 2

        for x in range(0, 6):
            while self.as_scores[x] < 20 and asi_points > 0:
                self.as_scores[x] += 1
                asi_points -= 1
        
        # list of int containing the ability score modifiers. You can calculate them like so.
        self.as_mods = []
        for x in self.as_scores:
            self.as_mods.append(floor((x - 10) / 2))

        # int containing the character's hit points. The numbers vary depending on the class.
        self.hp = (8 + self.as_mods[3]) + sum([randrange(1, 9) for x in range(0, self.level - 1)])
        
        # list of str containing armor proficiencies.
        self.armor_profs = ["Light Armor"]

        # list of str containing weapon proficiencies.
        self.weapon_profs = ["Simple weapons",
                             "Hand crossbows",
                             "Longswords",
                             "Rapiers",
                             "Shortswords"]

        # list of str containing tool proficiencies.
        self.tool_profs = ["Thieves' tools"]
        # Make sure you include the proficiencies from your background.
        for x in char_background.tool_profs:
            self.tool_profs.append(x)

        # list of str containing your saving throw proficiencies.
        self.saving_throws = ["Dexterity", "Intelligence"]

        # list of str containing your skills. Make sure they don't overlap with those from
        # your background.
        self.skills = []
        skill_choices = ["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation",
                         "Investigation", "Perception", "Performance", "Persuasion",
                         "Sleight of Hand", "Stealth"]
        for x in char_background.skill_profs:
            if x in skill_choices:
                skill_choices.remove(x)
        self.skills = char_background.skill_profs + sample(skill_choices, 4)

        # list of str containing your starting equipment.
        # If you need to pick a random weapon (like the fighter), you can just load
        # the items.json file in the resources folder and use a function like choice() or sample().
        self.equipment = []
        equipment_choices = [
            # Equipment A
            [["Rapier"], ["Shortsword"]],
            # Equipment B
            [["Shortbow", "Quiver of 20 arrows"], ["Shortsword"]],
            # Equipment C
            [["Burglar's pack"], ["Dungeoneer's Pack"], ["Explorer's Pack"]],
            # Equipment D
            [["Leather armor", "Dagger", "Dagger", "Thieve's tools"]]]
        for x in equipment_choices:
            for y in choice(x):
                self.equipment.append(y)

        # list of lists of str containing all the features granted by the class and it's subclasses.
        # These features should be appended based on the character's level.
        self.features = []
```

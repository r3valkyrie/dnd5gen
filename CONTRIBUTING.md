
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

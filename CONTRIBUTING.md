
# Contributing
hoo boi

### Adding backgrounds
Create a new python class in `dnd5gen/char_backgrounds`. The class should
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

